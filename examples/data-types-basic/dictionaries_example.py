#Dictionaries are data structures used to map arbitrary keys to values.

#Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

#Each element in a dictionary is represented by a key:value pair.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

#24
#42

# Trying to index a key that isn't part of the dictionary returns a KeyError.

primary = {
  "red": [255, 0, 0],
  "green": [0, 255, 0],
  "blue": [0, 0, 255],
}

print(primary["red"])
# [255, 0, 0]

#print(primary["yellow"])
# KeyError: 'yellow'

#Only immutable objects can be used as keys to dictionaries.
# Immutable objects are those that can't be changed.
# So far, the only mutable objects you've come across are lists and dictionaries.
# Trying to use a mutable object as a dictionary key causes a TypeError.

# bad_dict = {
#   [1, 2, 3]: "one two three",
# }
#TypeError: unhashable type: 'list'