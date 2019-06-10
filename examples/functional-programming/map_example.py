# The built-in functions map and filter are very useful higher-order functions that operate on
# lists (or similar objects called iterables).


#The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
#[16, 27, 38, 49, 60]

#We could have achieved the same result more easily by using lambda syntax

#To convert the result into a list, we used list explicitly.
result = list(map(lambda x: x+5, nums))
print(result)
#[16, 27, 38, 49, 60]


def multiply2(x):
  return x * 2


print(list(map(multiply2, [1, 2, 3, 4])))
# Output [2, 4, 6, 8]


print(list(map(lambda x : x*2, [1, 2, 3, 4])))
#Output [2, 4, 6, 8]