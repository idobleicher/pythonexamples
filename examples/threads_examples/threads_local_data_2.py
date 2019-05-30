#initialize the settings so all threads start with the same value, use a subclass and set the attributes in __init__().

import random
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):
    def __init__(self, value):
        logging.debug('Initializing %r', self)
        self.value = value

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()


## _init__() is invoked on the same object (note the id() value), once in each thread.
# (MainThread) Initializing <__main__.MyLocal object at 0x7fce5ddc3e28>
# (MainThread) value=1000
# (Thread-1  ) Initializing <__main__.MyLocal object at 0x7fce5ddc3e28>
# (Thread-1  ) value=1000
# (Thread-1  ) value=93
# (Thread-2  ) Initializing <__main__.MyLocal object at 0x7fce5ddc3e28>
# (Thread-2  ) value=1000
# (Thread-2  ) value=15
