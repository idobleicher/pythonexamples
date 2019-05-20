from itertools import accumulate, takewhile

# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# Some examples:

# chain - combines several iterables into one long one;

# accumulate - returns a running total of values in an iterable.

nums = list(accumulate(range(8)))
print(nums)
#[0, 1, 3, 6, 10, 15, 21, 28] 0 0+1 , 0+1+2 , 0+1+2+3 , 0+1+2+3+4

# takewhile - takes items from an iterable while a predicate function remains true;

nums2=[1,2,4,5,6,7,9]
print(list(takewhile(lambda x: x<= 6, nums2)))
#[1, 2, 4, 5, 6]

nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2 == 0, nums)
print(list(a))
# [2, 4, 6]
