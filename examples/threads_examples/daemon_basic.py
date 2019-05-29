import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
#marking as deamon
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

#Notice that the output does not include the "Exiting" message from the daemon thread,
# since all of the non-daemon threads (including the main thread) exit before the
# daemon thread wakes up from its two second sleep.

# (daemon    ) Starting
# (non-daemon) Starting
# (non-daemon) Exiting