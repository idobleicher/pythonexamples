#The function filter filters an iterable by removing items that don't match a
# predicate (a function that returns a Boolean).

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
#[22, 44]

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x<5,nums ))
print(res)
#[1, 2, 3, 0]
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))
# 2  # 2 ,3
