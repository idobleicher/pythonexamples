#1. accumulate(iter, func) :- This iterator takes two arguments, iterable target and the function which
# would be followed at each iteration of value in target.
# If no function is passed, addition takes place by default.
# If the input iterable is empty, the output iterable will also be empty.


import itertools


import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ",end="")
print (list(itertools.accumulate(li1)))
# The sum after each iteration is : [1, 5, 10, 17] (1 , 1+4 , 1+4+5 , 1+4+5+7

# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ",end="")
print (list(itertools.accumulate(li1,operator.mul)))
# The product after each iteration is : [1, 4, 20, 140] # 1 , 1*4 , 1*4*5 , 1*4*5*7


