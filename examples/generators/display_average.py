import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)


def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0

    while True:
        #data is following the consumer.send(data)
        data = yield
        print('In consumer. data {}'.format(data))
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield



if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for iteration in range(5):
        print('Iteration {} Producing...'.format(iteration))
        next(producer)

# #Iteration 0 Producing...
# Produced [6, 5, 7]
# In consumer. data [6, 5, 7]
# The running average is 6.0
# Iteration 1 Producing...
# Produced [1, 6, 4]
# In consumer. data [1, 6, 4]
# The running average is 4.833333333333333
# Iteration 2 Producing...
# Produced [6, 4, 5]
# In consumer. data [6, 4, 5]
# The running average is 4.888888888888889
# Iteration 3 Producing...
# Produced [8, 6, 5]
# In consumer. data [8, 6, 5]
# The running average is 5.25
# Iteration 4 Producing...
# Produced [4, 0, 5]
# In consumer. data [4, 0, 5]
# The running average is 4.8