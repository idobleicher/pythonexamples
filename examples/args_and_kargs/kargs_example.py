#*kwargs allows you to pass keyworded variable length of arguments to a function.

# You should use **kwargs if you want to handle named arguments in a function.
# Here is an example to get you going with it:

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
#name = yasoob
