#In this case, the resource in question is a mutex (e.g. a "Lock").
# Using context managers prevents a common source of deadlocks in multi-threaded programs which occur when a thread
# "acquires" a mutex and never "releases" it. Consider the following:

from threading import Lock
lock = Lock()

#Clearly lock.release() will never be called, causing all other threads calling do_something_dangerous() to become deadlocked.
# In our program, this is represented by never hitting the print('Got here') line.

def do_something_dangerous_wrong():
    lock.acquire()
    raise Exception('oops I forgot this code could raise exceptions')
    lock.release()

try:
    do_something_dangerous_wrong()
except:
    print('Got an exception')
lock.acquire()
print('Got here')

# This, however, is easily fixed by taking advantage of the fact that Lock is a context manager:

lock2 = Lock()

def do_something_dangerous_ok():
    with lock2:
        raise Exception('oops I forgot this code could raise exceptions')

try:
    do_something_dangerous_ok()
except:
    print('Got an exception')
lock.acquire()
print('Got here')