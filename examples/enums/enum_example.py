#Enumerations are created using the class syntax, which makes them easy to read and write.
#  An alternative creation method is described in Functional API.
#  To define an enumeration, subclass Enum as follows:

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

#Enumeration members have human readable string representations:
print(Color.RED)