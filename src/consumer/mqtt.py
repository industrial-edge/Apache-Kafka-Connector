# Copyright (c) Siemens 2021
# This file is subject to the terms and conditions of the MIT License.  
# See LICENSE file in the top-level directory

#=======================================
#    Requirements 
#=======================================

import paho.mqtt.client as mqtt

import globalconfig as config

#=======================================
#    MQTT Connection (IE Databus)
#=======================================

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))

# MQTT Connection Option
client = mqtt.Client()
client.username_pw_set(config.MQTT['USERNAME'], config.MQTT['PASSWORD'])
client.on_connect = on_connect

# Connect MQTT-Client to MQTT Broker (IE Databus)
client.connect(config.MQTT['HOST'], int(config.MQTT['PORT']), 60)
client.loop_start()

def publish (topic, msg):
    print('publish message: ' + msg + ' topic: ' + topic)
    client.publish(topic, msg)