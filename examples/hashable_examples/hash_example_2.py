# However, mutable objects such as lists and dictionaries do not have a hash method.

# That is one of the reasons why you cannot use that kind of objects as keys for dictionaries.

# What is important to note is that for immutable types, the hash value depends only on the data stored and
# not on the identity of the object itself.

# For instance, you can create two tuples with the same values, and see the differences:

var1 = (1, 2, 3)
var2 = (1, 2, 3)

print(id(var1))
print(id(var2))

#They are indeed different objects, however hash will return the same:
print(var1.__hash__())
print(var2.__hash__())

# This means that if you use them as dictionary keys, they are going to be
# indistinguishable (not able to be identified as different or distinct) from each other, for instance:

var3 = {var1: 'var1'}
print(var3[var2])
#var1
