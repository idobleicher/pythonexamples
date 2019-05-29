#At start-up, a Thread does some basic initialization and then calls its run() method,
# which calls the target function passed to the constructor.
# To create a subclass of Thread, override run() to do whatever is necessary.

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()

#Thread-1  ) running
# (Thread-2  ) running
# (Thread-3  ) running
# (Thread-4  ) running
# (Thread-5  ) running
