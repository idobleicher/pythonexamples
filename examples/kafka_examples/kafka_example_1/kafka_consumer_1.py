from kafka import KafkaConsumer
from json import loads
from examples.kafka_examples.kafka_example_1.kafka_producer_1 import topicname,bootstrap_servers_1


#---Consuming the data

 #auto_offet_reset=’earliest’:
# It handles where the consumer restarts reading after breaking down or being turned off and can
# be set either to earliest or latest.
# When set to latest, the consumer starts reading at the end of the log.
# When set to earliest, the consumer starts reading at the latest committed offset.

#Enable_auto_commit=True:
# makes sure the consumer commits its read offset every interval.

#auto_commit_interval_ms=1000ms:
# sets the interval between two commits.
# Since messages are coming in every x second, committing every second seems fair.

#group_id=’counters’:
# this is the consumer group to which the consumer belongs.
# A consumer needs to be part of a consumer group to make the auto commit work.

#The value deserializer deserializes the data into a common json format,
# the inverse of what our value serializer was doing.


group_id_1 = 'my-group'


# lambda could be used instead
def value_deserializer_1(x):
    if x:
        json_decode = loads(x.decode('utf-8'))
        return json_decode

consumer = KafkaConsumer(
    topicname,
     bootstrap_servers=bootstrap_servers_1,
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=group_id_1,
     value_deserializer=value_deserializer_1)


def main() :
    for message in consumer:
        messageVal = message.value
        print('Message value :{} '.format(messageVal))


if __name__ == '__main__':
    main()