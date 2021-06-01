# Copyright 2021 Siemens AG
# This file is subject to the terms and conditions of the MIT License.  
# See LICENSE file in the top-level directory

#=======================================
#    Requirements 
#=======================================

import paho.mqtt.client as mqtt

import globalconfig as config
import kafka

#=======================================
#    MQTT Connection (IE Databus)
#=======================================

# Subscribe to Topics after connection is established
def on_connect(client, userdata, flags, rc):
    print('Connected to MQTT-Broker with result code ' + str(rc))
    for topic in config.TOPICS:
        print('Subribed to Topic: ' + topic['MQTT'])
        client.subscribe(topic['MQTT'])

# Write Data to Apache Kafka after recieved message
def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    for topic in config.TOPICS:
        Topic = topic['MQTT']
        if(topic['MQTT'][-1] == '#'):
            Topic = topic['MQTT'][:-1]
        if(Topic in  msg.topic):
            kafka.produce(topic['KAFKA'], msg.payload, topic['KEY'])

# MQTT Connection Option
client = mqtt.Client()
client.username_pw_set(config.MQTT['USERNAME'], config.MQTT['PASSWORD'])
client.on_connect = on_connect
client.on_message = on_message

# Connect MQTT-Client to MQTT Broker (IE Databus)
client.connect(config.MQTT['HOST'], int(config.MQTT['PORT']), 60)

# Start MQTT-Client Thread
client.loop_forever()