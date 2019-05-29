
def some_func(func_args, *args, **kwargs):
    print("func_args:", func_args)

    for arg in args:
        print("arg in  *argv:", arg)

    for key, value in kwargs.items():
        print("keyarg {0} =  {1}".format(key, value))


func_arg="x"
args=("a" , "b")
kwargs = {"karg1": 3, "karg2": "two", "karg3": 5}

some_func(func_arg)
# func_args: x


print ("---------------------")

some_func(func_arg , args)
# func_args: x
# arg in  *argv: ('a', 'b')

print ("---------------------")

some_func(func_arg  , kwargs)
# func_args: x
# arg in  *argv: {'karg1': 3, 'karg2': 'two', 'karg3': 5