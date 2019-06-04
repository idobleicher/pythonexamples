#This example shows two simple partial objects for the function myfunc().
# The output of show_details() includes the func, args, and keywords attributes of the partial object.

import functools


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('  called myfunc with:', (a, b))


def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return


show_details('myfunc', myfunc)

print("--")
myfunc('a', 3)
print()

# Set a different default value for 'b', but require
# the caller to provide 'a'.
p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)

print("--")
p1('passing a')
p1('override b', b=5)
print()

print("--")
# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, 'default a', b=99)

show_details('partial with defaults', p2, True)
print("--")
p2()
print("--")
p2(b='override b')
print("--")
print()


#print('Insufficient arguments:')
# the first partial created is invoked without passing a value for a, causing an exceptio
#p1()