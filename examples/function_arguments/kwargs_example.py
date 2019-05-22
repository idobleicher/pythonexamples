# **kwargs (standing for keyword arguments) allows you to handle named arguments
# that you have not defined in advance.

# The keyword arguments return a dictionary in which the keys are the
# argument names, and the values are the argument values.

#The arguments returned by **kwargs are not included in *args.

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

#a and b are the names of the arguments that we passed to the function call.

my_func(2, 3, 4, 5, 6, a=7, b=8)
#{'a': 7, 'b': 8}