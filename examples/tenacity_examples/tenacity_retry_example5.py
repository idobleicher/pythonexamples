from tenacity import retry , stop_after_attempt , retry_if_result

#Custom Callbacks
#You can also define your own callbacks.
# The callback should accept one parameter called retry_state t
# hat contains all information about current retry invocation.

#For example, you can call a custom callback function after all retries failed,
# without raising an exception (or you can re-raise or do anything really)

def return_last_value(retry_state):
    """return the result of the last call attempt"""
    print("in return_last_value")
    result = retry_state.outcome.result()
   # return True
    return result

def is_false(value):
    """Return True if value is False"""
    print("in is_false")
    return value is False

# will return False after trying 3 times to get a different result
@retry(stop=stop_after_attempt(3),
       retry_error_callback=return_last_value,
       retry=retry_if_result(is_false))
def eventually_return_false():
    return False

print(eventually_return_false())
