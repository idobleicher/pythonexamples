#dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys.
#
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
#
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
#
# You can’t use lists as keys, since lists can be modified in place using index assignments,
# slice assignments, or methods like append() and extend().

#Note that dictionaries in python are not sorted.
# You can use collections.OrderedDict for this.
# Also to build correct sorting use sort/sorted functions with parameter
# key specified to sort the way you want

from itertools import product
myDict = {}
for x,y,z in product(range(10), range(10,20), range(20,30)):
    myDict[(x,y,z)] = sum([x,y,z])