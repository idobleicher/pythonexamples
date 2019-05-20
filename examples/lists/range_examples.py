#The range function creates a sequential list of numbers.
# The code below generates a list containing all of the integers, up to 10.

#The call to list is necessary because range by itself creates a range object,
#  and this must be converted to a list if you want to use it as one.
numbers = list(range(10))
print(numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums = list(range(5))
print(nums[4])
#4

# If range is called with one argument, it produces an object with values from 0 to that argument.
#If it is called with two arguments, it produces values from the first to the second.
numbers = list(range(3, 8))
print(numbers)
#[3, 4, 5, 6, 7]


print(range(20) == range(0, 20))
#True

nums = list(range(5, 8))
print(len(nums))
#3

#range can have a third argument, which determines the interval of the sequence produced.
# This third argument must be an integer.

numbers = list(range(5, 20, 2))
print(numbers)
# [5, 7, 9, 11, 13, 15, 17, 19]

nums = list(range(3, 15, 3))
print(nums[2])
# 9





