from tenacity import retry,wait_fixed,wait_random,wait_exponential,wait_random_exponential, wait_chain,stop_after_attempt,retry_if_exception_type
import datetime

#backoff

@retry(wait=wait_fixed(2))
def wait_2_s():
    print("Wait 2 second between retries")
    raise Exception

#wait_2_s()

@retry(wait=wait_random(min=1, max=2))
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")
    raise Exception

#wait_random_1_to_2_s()


#Wait strategy that applies exponential backoff.
@retry(wait=wait_exponential(multiplier=1, min=4, max=10))
def wait_exponential_1():
    print(datetime.datetime.now())
    print("Wait 2^x * 1 second between each retry starting with 4 seconds, then up to 10 seconds, then 10 seconds afterwards")
    raise Exception

#wait_exponential_1() #4 sec  , 8 ,10,10,10

@retry(wait=wait_fixed(3) + wait_random(0, 2))
def wait_fixed_jitter():
    print("Wait at least 3 seconds, and add up to 2 seconds of random delay")
    raise Exception

#wait_fixed_jitter()

@retry(wait=wait_random_exponential(multiplier=1, max=60))
def wait_exponential_jitter():
    print(datetime.datetime.now())
    print("Randomly wait up to 2^x * 1 seconds between each retry until the range reaches 60 seconds, then randomly up to 60 seconds afterwards")
    raise Exception

#wait_exponential_jitter()

#Sometimes it’s necessary to build a chain of backoffs.

@retry(wait=wait_chain(*[wait_fixed(3) for i in range(3)] +
                       [wait_fixed(7) for i in range(2)] +
                       [wait_fixed(9)]))
def wait_fixed_chained():
    print("Wait 3s for 3 attempts, 7s for the next 2 attempts and 9s for all attempts thereafter")
    raise Exception
#wait_fixed_chained()


@retry(
    wait=wait_exponential(1),
    reraise=True,
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type((IOError, ArithmeticError))
)
def wait_with_exception():
    print(datetime.datetime.now())
    raise  IOError

wait_with_exception()

