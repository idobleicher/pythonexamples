#https://www.geeksforgeeks.org/deque-in-python/

# Deque in Python
# Deque can be implemented in python using the module “collections“.
# Deque is preferred over list in the cases where we need quicker append and pop operations
# from both the ends of container, as deque provides an O(1) time complexity
# for append and pop operations as compared to list which provides O(n) time complexity.
#
# Operations on deque :
#
# 1. append() :- This function is used to insert the value in its argument to the right end of deque.
#
# 2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
#
# 3. pop() :- This function is used to delete an argument from the right end of deque. #
#
# 4. popleft() :- This function is used to delete an argument from the left end of deque.

# Python code to demonstrate working of
# append(), appendleft(), pop(), and popleft()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1,2,3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print ("The deque after appending at right is : ")
print (de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print ("The deque after appending at left is : ")
print (de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print ("The deque after deleting from right is : ")
print (de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print ("The deque after deleting from left is : ")
print (de)
