from tenacity import retry , retry_if_exception_type,retry_if_result,TryAgain,stop_after_attempt
from time import sleep
from examples.tenacity_examples.my_exceptions import MyException

#Whether to retry
#We have a few options for dealing with retries that raise specific or general exceptions, as in the cases here.
@retry(retry=retry_if_exception_type(exception_types=IOError))
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    sleep(1)
    raise IOError
    #raise Exception


#might_io_error()

def is_none_p(value):
    """Return True if value is None"""
    return value is None

#We can also use the result of the function to alter the behavior of retrying.
@retry(retry=retry_if_result(is_none_p))
def might_return_none():
    print("Retry with no wait if return value is None")
    sleep(1)


#might_return_none()

@retry(retry=(retry_if_result(is_none_p) | retry_if_exception_type()))
def might_return_none_with_exception():
    print("Retry forever ignoring Exceptions with no wait if return value is None")
    sleep(1)
    #raise Exception

#might_return_none_with_exception()

#It’s also possible to retry explicitly at any time by raising the TryAgain exception:
def something_else():
    return 23
@retry
def do_something():
    result = something_else()
    sleep(1)
    print("result" ,str(result))
    if result == 23:
       raise TryAgain

#do_something()

#Error Handling
#While callables that “timeout” retrying raise a RetryError by default,
# we can reraise the last attempt’s exception if needed:



@retry(reraise=True, stop=stop_after_attempt(3))
def raise_my_exception():
    print("in raise_my_exception")
    raise MyException("Fail")

try:
    print("in try before")
    raise_my_exception()
    print("in try after")
except MyException:
    print("in except")
    # timed out retrying
    pass


