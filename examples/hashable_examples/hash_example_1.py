# One of the complications of hash tables is how to implement the hash function in a reliable way.
# Immutable data types in Python come with a built-in method for computing their hash value,
# which is called __hash__.


# Let's see for example what happens with strings or tuples:
# strings and lists are reduced to integers
a = '123'
print(a.__hash__())

b = (1, 2, 3)
print(b.__hash__())

c = 1
print(c.__hash__())

d = 1.1
print(d.__hash__())

