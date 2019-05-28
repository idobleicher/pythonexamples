import threading
import time

def worker():
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print (threading.currentThread().getName(), 'Exiting')

def my_service():
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print( threading.currentThread().getName(), 'Exiting')


t = threading.Thread(name='my_service_x', target=my_service)
w = threading.Thread(name='worker_x', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

#worker_x Starting
# Thread-1 Starting
# my_service_x Starting
# worker_x Exiting
# Thread-1 Exiting
# my_service_x Exiting