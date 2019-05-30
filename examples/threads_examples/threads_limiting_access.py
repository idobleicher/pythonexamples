#Limiting Concurrent Access to Resources

#Sometimes it is useful to allow more than one worker access to a resource at a time, while still limiting the overall number.
# For example, a connection pool might support a fixed number of simultaneous connections,
# or a network application might support a fixed number of concurrent downloads.
#
# A Semaphore is one way to manage those connections.

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()

#In this example, the ActivePool class simply serves as a convenient way to track which threads are able to run at a given moment.
# A real resource pool would allocate a connection or some other value to the newly active thread,
# and reclaim the value when the thread is done. Here it is just used to hold the names
# of the active threads to show that only five are running concurrently.

#2019-05-30 09:12:48,029 (0 ) Waiting to join the pool
# 2019-05-30 09:12:48,029 (0 ) Running: ['0']
# 2019-05-30 09:12:48,030 (1 ) Waiting to join the pool
# 2019-05-30 09:12:48,030 (1 ) Running: ['0', '1']
# 2019-05-30 09:12:48,030 (2 ) Waiting to join the pool
# 2019-05-30 09:12:48,030 (3 ) Waiting to join the pool
# 2019-05-30 09:12:48,130 (0 ) Running: ['1']
# 2019-05-30 09:12:48,130 (2 ) Running: ['1', '2']
# 2019-05-30 09:12:48,131 (1 ) Running: ['2']
# 2019-05-30 09:12:48,131 (3 ) Running: ['2', '3']
# 2019-05-30 09:12:48,231 (2 ) Running: ['3']
# 2019-05-30 09:12:48,232 (3 ) Running: []




