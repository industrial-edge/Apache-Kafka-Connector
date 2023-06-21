# Implementation

- [Implementation](#implementation)
  - [App Configuration](#app-configuration)
    - [Bind-Mount Volume for configuration file](#bind-mount-volume-for-configuration-file)
    - [Default app configuration](#default-app-configuration)
    - [Read configuration file](#read-configuration-file)
  - [Connect to Databus](#connect-to-databus)
    - [MQTT-Client options](#mqtt-client-options)
    - [Connect MQTT-Client to Databus](#connect-mqtt-client-to-databus)
    - [Subscribe to Topics on Databus](#subscribe-to-topics-on-databus)
    - [Publish to Topic on Databus](#publish-to-topic-on-databus)
    - [On Message](#on-message)
  - [Connect to Apache Kafka](#connect-to-apache-kafka)
    - [Admin Client](#admin-client)
    - [Create Topic](#create-topic)
    - [Producer](#producer)
    - [Produce Message](#produce-message)
    - [Consumer](#consumer)
    - [Subscribe to Topics](#subscribe-to-topics)
    - [Poll loop](#poll-loop)

## App Configuration

### Bind-Mount Volume for configuration file

```yml
volumes:
    - './publish/:/publish/'
    - './cfg-data/:/cfg-data/'
```

### Default app configuration
```json
{
  "MQTT": {
    "HOST": "ie-databus",
    "PORT": "1883",
    "USERNAME": "edge",
    "PASSWORD": "edge"
  },
  "KAFKA": {
    "HOST": "192.168.253.143",
    "PORT": "9092"
  },
  "CONSUMER_TOPICS": [
    {
      "MQTT": "ie/d/kafka",
      "KAFKA": "EdgeDevice"
    }
  ],
  "PRODUCER_TOPICS": [
    {
      "MQTT": "ie/d/j/simatic/v1/s7c1/dp/r/#",
      "KAFKA": "EdgeDevice",
      "KEY": "S7-Connector"
    }
  ]
}
```

### Read configuration file
```python
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
```


## Connect to Databus

### MQTT-Client options
```python
client = mqtt.Client()
client.username_pw_set(config.MQTT['USERNAME'], config.MQTT['PASSWORD'])
client.on_connect = on_connect
```

### Connect MQTT-Client to Databus
```python
client.connect(config.MQTT['HOST'], int(config.MQTT['PORT']), 60)
```

### Subscribe to Topics on Databus
```python
def on_connect(client, userdata, flags, rc):
    print('Connected to MQTT-Broker with result code ' + str(rc))
    for topic in config.TOPICS:
        print('Subribed to Topic: ' + topic['MQTT'])
        client.subscribe(topic['MQTT'])
```

### Publish to Topic on Databus
```python
client.publish(topic, msg)
```

### On Message
```python
def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    //do something
```

## Connect to Apache Kafka

### Admin Client
```python
adminClient = AdminClient({'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT']})
```

### Create Topic
```python
new_topics = [NewTopic(topic['KAFKA'], num_partitions=3, replication_factor=1) for topic in config.TOPICS]
fs = adminClient.create_topics(new_topics)
```

### Producer
```python
producer = Producer({'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT']})
```

### Produce Message
```python
def produce(topic, data, key):
    producer.poll(0)
    producer.produce(topic, data, key=key, callback=delivery_report)
```

### Consumer
```python
consumer = Consumer({
    'bootstrap.servers': config.KAFKA['HOST'] + ':' + config.KAFKA['PORT'],
    'group.id': 'edgedevice',
    'auto.offset.reset': 'earliest'
    })
```

### Subscribe to Topics
```python
kafkaTopics = [topic['KAFKA'] for topic in config.TOPICS]
    
consumer.subscribe(kafkaTopics)
```

### Poll loop
```python
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
```
