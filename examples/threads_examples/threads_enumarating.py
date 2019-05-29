#It is not necessary to retain an explicit handle to all of the daemon threads in order to ensure they
# have completed before exiting the main process.
# enumerate() returns a list of active Thread instances.

# The list includes the current thread, and since joining the current thread is not allowed (it introduces a deadlock situation),
# it must be skipped.

import random
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker():
    """thread worker function"""
    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')
    return

for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()

for t in threading.enumerate():
    if t is main_thread:
        # The list includes the current thread, and since joining the
        # current thread is not allowed (it introduces a deadlock situation) - must be skipped
        continue
    logging.debug('joining %s', t.getName())
    t.join()

    #
# (Thread-1  ) sleeping 3
# (Thread-2  ) sleeping 2
# (Thread-3  ) sleeping 5
# (MainThread) joining Thread-1
# (Thread-2  ) ending
# (Thread-1  ) ending
# (MainThread) joining Thread-3
# (Thread-3  ) ending
# (MainThread) joining Thread-2

