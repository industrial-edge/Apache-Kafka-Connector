# Copyright 2021 Siemens AG
# This file is subject to the terms and conditions of the MIT License.  
# See LICENSE file in the top-level directory

#=======================================
#    Requirements 
#=======================================

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

import globalconfig as config
import mqtt

#=======================================
# Kafka
#=======================================

# Create Topic
adminClient = AdminClient({'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT']})
    
new_topics = [NewTopic(topic['KAFKA'], num_partitions=3, replication_factor=1) for topic in config.TOPICS]

fs = adminClient.create_topics(new_topics)

# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print('Topic {} created'.format(topic))
    except Exception as e:
        print('Failed to create topic {}: {}'.format(topic, e))

# Create Consumer instance
consumer = Consumer({
    'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT'],
    'group.id': 'edgedevice',
    'auto.offset.reset': 'earliest'
    })
print('consumer created')

kafkaTopics = [topic['KAFKA'] for topic in config.TOPICS]
    
consumer.subscribe(kafkaTopics)

# Poll loop
while True:
    msg = consumer.poll(timeout=1.0)

    if msg is None:
        continue
    if msg.error():
        print('Consumer error: {}'.format(msg.error()))
        continue
    print(msg.topic())
    for topic in config.TOPICS:
        if(topic['KAFKA'] == msg.topic()):
            value = msg.value().decode('utf-8')
            print('Received message: {}'.format(value))
            mqtt.publish(topic['MQTT'], value)
       

consumer.close()