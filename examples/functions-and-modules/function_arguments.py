
# Technically, parameters are the variables in a function definition,
#  and arguments are the values put into parameters when functions are called.

# Function arguments can be used as variables inside the function definition.
# However, they cannot be referenced outside of the function's definition.
# This also applies to other variables created inside a function.


def function1(variable):
    variable += 1
    print(variable)


function1(7)
# 8

# print(variable)
# NameError: name 'variable' is not defined


def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
# spam!


# You can also define functions with more than one argument; separate them with commas.

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)


print_sum_twice(5, 8)
# 13
# 13


def even(x):
    if x % 2 == 0:
        print ("Yes")
    else:
        print("No")


even(1)
# No
even(2)
# Yes




