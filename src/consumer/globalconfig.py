# Copyright (c) Siemens 2021
# This file is subject to the terms and conditions of the MIT License.
# See LICENSE file in the top-level directory

#=======================================
#    Requirements
#=======================================

import json

#=======================================
#    Define Variables
#=======================================
configJson = json.loads('{}')
MQTT = json.loads('{}')
KAFKA = json.loads('{}')

#=======================================
#    Init Programm using Configuration file
#=======================================
print('Global App Configuration')


def readJsonFile(path):
    with open(path) as file:
        configJson = json.load(file)
        return configJson


print('Global: reading configuration file')
try:
   configuration = readJsonFile('./config/config-default.json')
   configJson = readJsonFile('/cfg-data/config.json')
except:
   print('Warning, using default configuration because reading config.json file failed')

if 'MQTT' in configJson:
   MQTT['HOST'] = configJson['MQTT']['HOST']
   MQTT['PORT'] = configJson['MQTT']['PORT']
   MQTT['USERNAME'] = configJson['MQTT']['USERNAME']
   MQTT['PASSWORD'] = configJson['MQTT']['PASSWORD']
else:
   print('No MQTT Configuration provided')
   MQTT['HOST'] = configuration['MQTT']['HOST']
   MQTT['PORT'] = configuration['MQTT']['PORT']
   MQTT['USERNAME'] = configuration['MQTT']['USERNAME']
   MQTT['PASSWORD'] = configuration['MQTT']['PASSWORD']

if 'KAFKA' in configJson:
   KAFKA['HOST'] = configJson['KAFKA']['HOST']
   KAFKA['PORT'] = configJson['KAFKA']['PORT']
else:
   print('No Kafka Configuration provided')
   KAFKA['HOST'] = configuration['KAFKA']['HOST']
   KAFKA['PORT'] = configuration['KAFKA']['PORT']
   
if 'CONSUMER_TOPICS' in configJson:
   TOPICS = configJson['CONSUMER_TOPICS']
else:
   print('No TOPICS Configuration provided')
   TOPICS = configuration['CONSUMER_TOPICS']
