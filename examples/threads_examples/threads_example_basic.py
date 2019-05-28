#The simplest way to use a Thread is to instantiate it with a target function and call start() to let it begin working.

import threading
def func_worker():
    """thread worker function"""
    print ('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=func_worker)
    threads.append(t)
    t.start()

# Worker
# Worker
# Worker
# Worker
# Worker