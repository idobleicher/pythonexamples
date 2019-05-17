# Python allows to have function with varying number of arguments.

# Using *args as a function parameter enables you to pass an arbitrary number
#  of arguments to that function.

# The arguments are then accessible as the TUPLE args in the body of the function.

# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.


def function1(named_arg, *args):
   print(named_arg)
   print(args)


function1(1, 2, 3, 4, 5)
# 1
#  (2, 3, 4, 5)


