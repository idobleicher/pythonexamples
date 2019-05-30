#To find out whether another thread has acquired the lock without holding up the current thread,
# pass False for the blocking argument to acquire().
#
# In the next example, worker() tries to acquire the lock three separate times, and counts how many attempts it has
# to make to do so.
#
# In the mean time, lock_holder() cycles between holding and releasing the lock, with short pauses in each state used to simulate load.

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)
    return


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired', num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


lock = threading.Lock()

holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker, args=(lock,), name='Worker')
worker.start()

#it takes worker() more than three iterations to acquire the lock three separate times.

#$ python threading_lock_noblock.py
#
# (LockHolder) Starting
# (LockHolder) Holding
# (Worker    ) Starting
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 1: Acquired
# (Worker    ) Trying to acquire
# (LockHolder) Holding
# (Worker    ) Iteration 2: Not acquired
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 3: Acquired
# (LockHolder) Holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 4: Not acquired
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 5: Acquired
# (Worker    ) Done after 5 iterations

