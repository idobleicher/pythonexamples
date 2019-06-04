#Acquiring Function Properties for Decorators

#Updating the properties of a wrapped callable is especially useful
# when used in a decorator, since the transformed function ends up with properties of the original “bare” function.

#functools provides a decorator, wraps(), that applies update_wrapper() to the decorated function

import functools


def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    print()



def simple_decorator(f):
    print ("in simple decorator")
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('  decorated:', (a, b))
        print('  ', end=' ')
        return f(a, b=b)
    return decorated


def myfunc(a, b=2):
    "myfunc() is not complicated"
    print('  myfunc:', (a, b))
    return


# The raw function
print("-------------------")
show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
print("-------------------")
myfunc('unwrapped, passing b', 3)
print()
print("-------------------")



# Wrap explicitly
print("-------------------")
wrapped_myfunc = simple_decorator(myfunc)

show_details('wrapped_myfunc', wrapped_myfunc)
print("   ---")
wrapped_myfunc()
print("   ---")
wrapped_myfunc('args to wrapped', 4)
print()
print("-------------------")

# Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return

print("-------------------")
show_details('decorated_myfunc', decorated_myfunc)
print("------ ")
decorated_myfunc()
print("------ ")
decorated_myfunc('args to decorated', 4)
print("-------------------")