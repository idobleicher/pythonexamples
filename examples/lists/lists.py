words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)

# Typically, a list will contain items of a single item type, but it
# is also possible to include several different types.

# Lists can also be nested within other lists.

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
# 0
print(things[2])
# [1, 2, 3]
print(things[2][2])
# 3

# Indexing out of the bounds of possible list values causes an IndexError.

#Some types, such as strings, can be indexed like lists.
#  Indexing strings behaves as though you are indexing a
#  list containing each character in the string.

#For other types, such as integers, indexing them isn't possible, and it causes a TypeError
str = "Hello world!"
print(str[6])
# w

print(len(["a", "b"]))
# 2


