#Thread-specific Data

#While some resources need to be locked so multiple threads can use them,
# others need to be protected so that they are hidden from view in threads that do not “own” them.
# The local() function creates an object capable of hiding values from view in separate threads.

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


local_data = threading.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

 #Notice that local_data.value is not present for any thread until it is set in that thread.

 #(MainThread) No value yet
# (MainThread) value=1000
# (Thread-1  ) No value yet
# (Thread-1  ) value=74
# (Thread-2  ) No value yet
# (Thread-2  ) value=26

