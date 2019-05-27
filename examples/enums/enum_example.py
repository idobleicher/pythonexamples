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

#while their repr has more information:
print(repr(Color.RED))
#<Color.RED: 1>

#The type of an enumeration member is the enumeration it belongs to:
print(type(Color.RED))
#<enum 'Color'>

print(isinstance(Color.GREEN, Color))
#True

#Enum members also have a property that contains just their item name:
print(Color.RED.name)
#RED
print("--------------")

#Enumerations support iteration, in definition order:

class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3

for shake in Shake:
    print(shake)

Shake.VANILLA
Shake.CHOCOLATE
Shake.COOKIES
Shake.MINT

#Enumeration members are hashable, so they can be used in dictionaries and sets:
apples = {}
apples[Color.RED] = 'red delicious'
apples[Color.GREEN] = 'granny smith'
print(apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'})
#TRUE

print ("~~~~~~~~~~~~~~")
print(list(Color))
print ("~~~~~~~~~~~~~~")

#Programmatic access to enumeration members and their attributes

print(Color.RED)
#Color.RED

#If you want to access enum members by name, use item access:
print(Color['RED'])
#Color.RED

#If you have an enum member and need its name or value:
member = Color.RED
print(member.name)
#RED
print(member.value)
#1


#two enum members are allowed to have the same value.

#@enum.unique - A class decorator specifically for enumerations.
#ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

print(Color.RED is Color.RED)
print(Color.RED is not Color.BLUE)