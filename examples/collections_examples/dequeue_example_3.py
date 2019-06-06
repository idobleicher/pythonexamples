# 9. extend(iterable) :- This function is used to add multiple values at the right end of deque.
# The argument passed is an iterable.
#
# 10. extendleft(iterable) :- This function is used to add multiple values at the left end of deque.
# The argument passed is an iterable. Order is reversed as a result of left appends.
#
# 11. reverse() :- This function is used to reverse order of deque elements.
#
#
# 12. rotate() :- This function rotates the deque by the number specified in arguments.
# If the number specified is negative, rotation occurs to left. Else rotation is to right.

# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
de.extendleft([7,8,9])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print (de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print (de)
