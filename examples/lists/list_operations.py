nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
# [7, 7, 5, 7, 7]

nums = [1, 2, 3]
print(nums + [4, 5, 6])
# [1, 2, 3, 4, 5, 6]

print(nums * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
# True
print("egg" in words)
# True
print("tomato" in words)
# False
print("tomato" not in words)
# True

nums = [1, 2, 3]
print(not 4 in nums)
# True
print(4 not in nums)
# True
print(not 3 in nums)
# False
print(3 not in nums)
# False


letters = ['a', 'b', 'z']
if "z" in letters:
    print("Yes")

