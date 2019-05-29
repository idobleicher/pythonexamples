
#Using *args and **kwargs to call a function


def fun_with_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

#first    with *args - tuple
args = ("two", 3, 5)
fun_with_args_kwargs(*args)
# arg1: two
# arg2: 3
# arg3: 5

 # now with **kwargs: dictionary
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
fun_with_args_kwargs(**kwargs)
# arg1: 5
# arg2: two
# arg3: 3
