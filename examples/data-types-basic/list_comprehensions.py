# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
cubes = [i**3 for i in range(5)]
print(cubes)
#[0, 1, 8, 27, 64]

nums = [i*2 for i in range(10)]
print(nums)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#A list comprehension can also contain an if statement to enforce a condition on values in the list.
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
#[0, 4, 16, 36, 64]

#T rying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.
# even = [2*i for i in range(10**100)]
#This issue is solved by generators, which are covered in the next module.

a = [x * 10 for x in range(5  , 9)]
print(a)
# [50, 60, 70, 80]

