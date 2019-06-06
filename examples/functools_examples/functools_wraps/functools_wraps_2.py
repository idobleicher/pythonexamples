from functools import wraps



def decorator_func(orig_func) :
    print ("in decor func init")
    some_deco_field = "x"

    @wraps(orig_func)
    def wrapper(param1):
        print("in wrapper. param1:" , str(param1))
        print("in wrapper. some_deco_field:", str(some_deco_field))
        orig_func(param1)
        return

    return wrapper



@decorator_func
def some_function(param1):
    print("in some function.Param 1:" , str(param1))


some_function(1)
some_function(2)