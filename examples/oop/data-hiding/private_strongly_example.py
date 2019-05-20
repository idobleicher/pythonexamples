# Strongly private methods and attributes have a DOUBLE underscore at the beginning of their names.
#  This causes their names to be mangled, which means that they can NOT be
#  accessed from outside the class.

# The purpose of this is NOT to ensure that they are kept private, but to avoid bugs if there
#  are subclasses that have methods or attributes with the same names.

# Name mangled methods can still be accessed externally, but by a different name.

#  The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

#Basically, Python protects those members by internally changing the name to include the class name.

class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
#7

print(s._Spam__egg)
#7

#print(s.__egg)
#AttributeError: 'Spam' object has no attribute '__egg'