print(min(1, 2, 3, 4, 0, 2, 1))
#0
print(max([1, 4, 9, 2, 5, 6, 8]))
#9
print(abs(-99))
#99
print(abs(42))
#42
print(sum([1, 2, 3, 4, 5]))
#15

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
#30


nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
#44
