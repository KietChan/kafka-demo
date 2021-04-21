#!/bin/bash
cd /home/ubuntu/
git clone https://github.com/KietChan/kafka-demo
apt install openjdk-11-jre-headless -y
tar -zxvf kafka-demo/shells/kafka_2.12-2.7.0.tgz
rm -rf kafka-demo
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
echo "advertised.listeners=PLAINTEXT://$(curl https://ipinfo.io/ip):9092" >> ./kafka_2.12-2.7.0/config/server.properties
./kafka_2.12-2.7.0/bin/zookeeper-server-start.sh ./kafka_2.12-2.7.0/config/zookeeper.properties &>/dev/null &
./kafka_2.12-2.7.0/bin/kafka-server-start.sh ./kafka_2.12-2.7.0/config/server.properties &>/dev/null &
./kafka_2.12-2.7.0/bin/kafka-topics.sh --create --topic tasks --bootstrap-server localhost:9092 --partitions 3
