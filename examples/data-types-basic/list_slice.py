
# List slices provide a more advanced way of retrieving values from a list.
# Basic list slicing involves indexing a list with two colon-separated integers.
# This returns a new list containing all the values in the old list between the indices.

# Slicing can also be done on tuples.

nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(nums[2:6])
# [[12, 13, 14, 15] #0th - to 6th

print(nums[3:8])
# [13, 14, 15, 16, 17] #3th to 7th

print(nums[0:1])
#[10] - 0th


print("--------------")
# If the first number in a slice is omitted, it is taken to be the start of the list.
print(nums[:7])
# [10, 11, 12, 13, 14, 15, 16]
# If the second number is omitted, it is taken to be the end.
print(nums[7:])
# [17, 18, 19]

print("--------------")
# List slices can also have a third number, representing the step,
# to include only alternate values in the slice.

print(nums[::2])
# [10, 12, 14, 16, 18]


print(nums[2:8:3])
# [2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.
# [12, 15]
print("!!--------------")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1::4])
#[1, 25, 81]
print("!!!--------------")

# Negative values can be used in list slicing (and normal list indexing).#
# When negative values are used for the first and second values in a slice (or a normal index),
# they count from the end of the list.
print("~~--------------")
print(nums[1:-1])
# [11, 12, 13, 14, 15, 16, 17, 18] #1th to len-1
print("~~--------------")
# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.
print(squares[7:5:-1])
#[49, 36]

print(squares[::-1])
#[81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
