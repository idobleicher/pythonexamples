import threading
#Normal Lock objects cannot be acquired more than once, even by the same thread.
# This can introduce undesirable side-effects if a lock is accessed by more than one function in the same call chain.

lock = threading.Lock()

print ('First try :', lock.acquire())
print ('Second try:', lock.acquire(0))

#In this case, since both functions are using the same global lock, and one calls the other,
# the second acquisition fails and would have blocked using the default arguments to acquire().


#First try : True
#Second try: False


#In a situation where separate code from the same thread needs to “re-acquire” the lock, use an RLock instead.

rlock = threading.RLock()

print ('Rlock First try :', rlock.acquire())
print ('Rlock Second try:', rlock.acquire(0))
#The only change to the code from the previous example was substituting RLock for Lock.

#Rlock First try : True
#Rlock Second try: True