#map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)

squared2 = list(map(lambda x: x ** 2, items))
print(squared2)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

print("------------------------")
#Instead of a list of inputs we can even have a list of functions!
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
print("------------------------")

#filter creates a list of elements for which a function returns true
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
print("------------------------")

#Reduce useful function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list.
# For example, if you wanted to compute the product of a list of integers.
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24 (1*2*3*4)

