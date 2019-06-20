from collections import namedtuple

# A named tuple is a tuple.

# It does everything a tuple can.
#
# But it's more than just a tuple.
#
# It's a specific subclass of a tuple that is programmatically created to your specification,
# with named fields and a fixed length.

class_name = 'ANamedTuple'
fields = 'foo bar baz'
ANamedTuple = namedtuple(class_name, fields)

ant = ANamedTuple(1, 'bar', [])

print(ant)
print(ant.foo)

ant.baz.append('anything')
print(ant.baz)