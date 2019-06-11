#Tenacity is an Apache 2.0 licensed general-purpose retrying library, written in Python,
# to simplify the task of adding retry behavior to just about anything.

#The simplest use case is retrying a flaky function whenever an Exception occurs until a value is returned.

import random
from tenacity import retry,stop_after_attempt ,stop_after_delay
from time import sleep

#the default behavior is to retry forever without waiting when an exception is raised.
@retry
def do_something_unreliable():
    rand_num = random.randint(0, 10)
    print(rand_num)
    if rand_num > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

print(do_something_unreliable())
#7
# 8
# 6
# 10
# 2
# 1
# Awesome sauce!


print("----------------------------------------------")
@retry(stop=stop_after_attempt(7))
def stop_after_7_attempts():
    print("Stopping after 7 attempts")
    raise Exception

try:
    stop_after_7_attempts()
except:
    print("Error occurred")



print("----------------------------------------------")
@retry(stop=stop_after_delay(5))
def stop_after_5_s():
    print("Stopping after 5 seconds")
    sleep(1)
    raise Exception


try:
    stop_after_5_s()
except:
    print("Error occurred")

print("----------------------------------------------")

@retry(stop=(stop_after_delay(5) | stop_after_attempt(3)))
def stop_after_5_s_or_3_retries():
    print("Stopping after 5 seconds or 3 retries")
    raise Exception

try:
    stop_after_5_s_or_3_retries()
except:
    print("Error occurred")
