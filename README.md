# Apache Kafka Connector

Connect Industrial Edge Device to Apache Kafka 

- [Apache Kafka Connector](#apache-kafka-connector)
  - [Description](#description)
    - [Overview](#overview)
    - [General task](#general-task)
  - [Requirements](#requirements)
    - [Used Components](#used-components)
    - [TIA Project](#tia-project)
    - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Implementation](#implementation)
  - [Documentation](#documentation)
  - [Contribution](#contribution)
  - [Licence and Legal Information](#licence-and-legal-information)

## Description

### Overview

The Apache Kafka Connector connects to the IE Databus and Apache Kafka. The Connector can subcribes to MQTT Topics on IE Databus and produces messages (events, records) on a Kafka Topic. Also the Connector can consume messages from a Kafka Topic and publishes messages to MQTT Topics on IE Databus.

### General task

This example shows how to connect your Industrial Edge Device to Apache Kafka. Therefore a SIMATIC PLC is used as datasource. The S7-Connector reads the data from the PLC and publish them on IE Databus. The Apache Kafka Connector consists of two services, the "kafka-producer" and "kafka-consumer". The "kafka-producer" subscribes to the IE Databus, gets data from S7-Connector and produces messages in an Apache Kafka Broker's topic. The "kafka-consumer" subscribes to the same topic on the Apache Kafka Broker and publishes the data an other topic on IE Databus. The IE Flow Creator can be used to verify the data exchange between Industrial Edge and Apache Kafka.

![Overview](docs/graphics/overview.png)

## Requirements

### Used Components

- OS: Windows or Linux
- Docker minimum V18.09
- Docker Compose V2.0 – V2.4
- Industrial Edge App Publisher (IEAP) V1.2.8
- Industrial Edge Management (IEM) V1.2.16
  - S7 Connector V1.2.26
  - S7 Connector Configurator 1.2.38
  - IE Databus V1.2.16
  - IE Databus Configurator V1.2.29
  - IE App Configuration Service V1.0.5
- Industrial Edge Device (IED) V1.2.0-56
- TIA Portal V16 
- PLC: CPU 1512 FW 2.8.3

### TIA Project

The used TIA Portal project can be found in the [miscellaneous repository](https://github.com/industrial-edge/miscellaneous) in the tank application folder and is also used for several further application examples:

- [Tia Tank Application](https://github.com/industrial-edge/miscellaneous/tree/main/tank%20application)

### Prerequisites
Before using this application make sure you have a running Apache Kafka Broker. To setup up a test environment either follow the [Apache Kafka Quickstart guide](https://kafka.apache.org/quickstart) or use the provided [docker-compose.yml](./test/kafka-broker/docker-compose.yml) as described [here](./docs/installation.md#apache-kafka-broker-test-environment)

## Installation

You can find the further information about the following steps in the [docs](./docs)

- [Build application](docs/installation.md#build-application)
- [Upload application to Industrial Edge Management](docs/installation.md#upload-application-to-industrial-edge-management)
- [Configure and install application to Industrial Edge Device](docs/installation.md#install-application-on-industrial-edge-device)

## Usage

Connect your Industrial Edge Device to a PLC as datasource over the network.

Provide a Apache Kafka Broker (see [Prerequisites](#prerequisites)) that is accessible for the Industrial Edge Device over the network

Use e.g. IE Flow Creator to verify data exchange to and from Apache Kafka Broker.

![Test](./docs/graphics/test.png)

## Implementation

How to implement a Apache Kafka Producer and Consumer as well as further details about the source code can be found in the [implementation section](./docs/implementation.md).

- [App Configuration](./docs/implementation.md#app-configuration)
- [Connect to IE Databus](./docs/implementation.md#connect-to-ie-databus)
- [Connect to Apache Kafka](./docs/implementation.md#connect-to-apache-kafka)

## Documentation

- Add links to additional documentation here
  
- Here is a link to the [docs](docs/) of this application example.
- You can find further documentation and help in the following links
  - [Industrial Edge Hub](https://iehub.eu1.edge.siemens.cloud/#/documentation)
  - [Industrial Edge Forum](https://www.siemens.com/industrial-edge-forum)
  - [Industrial Edge landing page](https://new.siemens.com/global/en/products/automation/topic-areas/industrial-edge/simatic-edge.html)
  - [Industrial Edge GitHub page](https://github.com/industrial-edge)
  
## Contribution

Thanks for your interest in contributing. Anybody is free to report bugs, unclear documentation, and other problems regarding this repository in the Issues section or, even better, is free to propose any changes to this repository using Merge Requests.

## Licence and Legal Information

Please read the [Legal information](LICENSE.md).
