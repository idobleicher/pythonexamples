from time import sleep
from json import dumps
from kafka import KafkaProducer


# ---- Producing------
#bootstrap_servers=[‘localhost:9092’]: sets the host and port the producer should contact to
# bootstrap initial cluster metadata.
# It is not necessary to set this here, since the default is localhost:9092.

#serlizer =  function of how the data should be serialized before sending to the broker

def value_seralizer_1(x):
    json_bin = dumps(x).encode('utf-8')    #lambda could be use
    return json_bin

bootstrap_servers_1 = ['localhost:9092']

producer = KafkaProducer(bootstrap_servers=bootstrap_servers_1,
                         value_serializer= value_seralizer_1)

#If you want to make sure the message is received by the broker, it’s advised to include a callback.

topicname = "testTopic"

def main():
    for e in range(10):
        data = {'number' : e}
        print ("sending:" , data)
        producer.send(topicname, value=data)
        sleep(2)


if __name__ == '__main__':
    main()

