#Most programs do not use print to debug.
# The logging module supports embedding the thread name in every log message using the
# formatter code %(threadName)s. Including thread names in log messages makes it easier to trace those messages back to their source.

#logging is also thread-safe, so messages from different threads are kept distinct in the output.


import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# [DEBUG] (worker    ) Starting
# [DEBUG] (Thread-1  ) Starting
# [DEBUG] (my_service) Starting
# [DEBUG] (worker    ) Exiting
# [DEBUG] (Thread-1  ) Exiting
# [DEBUG] (my_service) Exiting