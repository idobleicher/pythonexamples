# Data Hiding - weekly private

#Weakly private methods and attributes have a single underscore at the beginning.

#This signals that they are private, and shouldn't be used by external code.
#  However, it is mostly only a convention, and does not stop external code from accessing them.

#Its only actual effect is that
# from module_name import *
#  won't import variables that start with a single underscore.

class Queue:
    def __init__(self, contents):
        #single underscore
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    # The __repr__ magic method is used for string representation of the instance.
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
# Queue([1, 2, 3])

queue.push(0)
print(queue)
#Queue([0, 1, 2, 3])

queue.pop()
print(queue)
# Queue([0, 1, 2])

# The attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
print(queue._hiddenlist)
# [0, 1, 2]
