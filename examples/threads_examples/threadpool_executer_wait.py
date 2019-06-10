#The wait() function would return a named tuple which contains two set –
# one set contains the futures which completed (either got result or exception)
# and the other set containing the ones which didn’t complete.

#We can control the behavior of the wait function by defining when it should return.
# We can pass one of these values to the return_when param of the function:
# FIRST_COMPLETED,
# FIRST_EXCEPTION
# and ALL_COMPLETED.
# By default, it’s set to ALL_COMPLETED,
# so the wait function returns only when all futures complete
#But using that parameter, we can choose to return when
# the first future completes or first exception encounters.

from concurrent.futures import ThreadPoolExecutor, wait,FIRST_COMPLETED,ALL_COMPLETED
from time import sleep
from random import randint

def return_after_5_secs(num):
    sleep(randint(1, 5))
    return "Return of {}".format(num)

pool = ThreadPoolExecutor(5)
futures = []
for x in range(5):
    futures.append(pool.submit(return_after_5_secs, x))


#print(wait(futures))
print(wait(futures ,return_when=FIRST_COMPLETED))
print(wait(futures ,return_when=ALL_COMPLETED))