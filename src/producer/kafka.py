# Copyright (c) Siemens 2021
# This file is subject to the terms and conditions of the MIT License.  
# See LICENSE file in the top-level directory

#=======================================
#    Requirements 
#=======================================

from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

import globalconfig as config

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

# Create Producer instance
producer = Producer({'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT']})
print('producer created')

def delivery_report(err, msg):
    ''' Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). '''
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Produce Message
def produce(topic, data, key):
    producer.poll(0)
    producer.produce(topic, data, key=key, callback=delivery_report)

    