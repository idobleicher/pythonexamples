# Often used in conditional statements, all and any take a list as an argument,
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")



#The function enumerate can be used to iterate through the values and indices of a list simultaneously.
for v in enumerate(nums):
   print(v)
   # (0, 55)
   # (1, 44)
   # (2, 33)
   # (3, 22)
   # (4, 11)


nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)
  #2