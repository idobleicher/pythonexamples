from tenacity import retry,stop_after_attempt,before_log,after_log,before_sleep_log
from time import sleep
import logging
import sys
from examples.tenacity_examples.my_exceptions import MyException


#Before and After Retry, and Logging
#It’s possible to execute an action before any attempt of calling the function by using the before callback function:



logging.basicConfig(filename='tenacity_retry_example4.log', level=logging.DEBUG)
logging.warning('starting')

logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), before=before_log(logger, logging.DEBUG))

def raise_my_exception():
    raise MyException("Fail")

#raise_my_exception()

#In the same spirit, It’s possible to execute after a call that failed:
@retry(stop=stop_after_attempt(3), after=after_log(logger, logging.DEBUG))
def raise_my_exception_2():
    raise MyException("Fail")

#raise_my_exception_2()

#It’s also possible to only log failures that are going to be retried.
# Normally retries happen after a wait interval, so the keyword argument is called before_sleep:
@retry(stop=stop_after_attempt(3),
       before_sleep=before_sleep_log(logger, logging.DEBUG))
def raise_my_exception_3():
    raise MyException("Fail")

#raise_my_exception_3()

#Statistics
#ou can access the statistics about the retry made over a
# function by using the retry attribute attached to the function and its statistics attribute:
@retry(stop=stop_after_attempt(3))
def raise_my_exception_4():
    raise MyException("Fail")

try:
    raise_my_exception_4()
except Exception:
    pass

print(raise_my_exception_4.retry.statistics)
