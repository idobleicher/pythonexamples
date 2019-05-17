# Although they are created differently from normal variables,
#  functions are just like any other kind of value.
# They can be assigned and reassigned to variables, and later referenced by those names


def multiply(x, y):
    return x * y


a = 4
b = 7
operation = multiply
print(operation(a, b))
# 28

# Functions can also be used as arguments of other functions.
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
# 30 = ((5 +10) + ( 5 + 10))

def multiply(x, y):
  return x * y

print(do_twice(multiply, 2, 3))
# 36 = ((2 *3) * ( 2 * 3) )


def square(x):
    return x * x


def test(func, x):
    print(func(x))


test(square , 2)
#4


