#Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.
#
# reduce() is defined in “functools” module, accumulate() in “itertools” module.

# reduce() stores the intermediate result and only returns the final summation value.
# Whereas, accumulate() returns a list containing the intermediate results.
# The last number of the list returned is summation value of the list.

# reduce(fun,seq) takes function as 1st and sequence as 2nd argument.
# In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.

# python code to demonstrate summation
# using reduce() and accumulate()

# importing itertools for accumulate()
import itertools

# importing functools for reduce()
import functools

# initializing list
lis = [ 1, 3, 4, 10, 4 ]

# priting summation using accumulate()
print ("The summation of list using accumulate is :",end="")
print (list(itertools.accumulate(lis,lambda x,y : x+y)))

# priting summation using reduce()
print ("The summation of list using reduce is :",end="")
print (functools.reduce(lambda x,y:x+y,lis))
