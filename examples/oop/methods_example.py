#Classes can have other methods defined to add functionality to them.
#Remember, that all methods must have self as their first parameter.
#These methods are accessed using the same dot syntax as attributes.

#Classes can also have class attributes, created by assigning variables within the body of the class.
# These can be accessed either from instances of the class, or the class itself.like static

class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")

print(fido.name)
fido.bark()
# Fido
# Woof!

print(fido.legs)
print(Dog.legs)
#4
#4
# Class attributes are shared by all instances of the class.


class Student:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hi from " + self.name)

s1 = Student("Amy")
s1.sayHi()
#Hi from Amy

#Trying to access an attribute of an instance that isn't defined causes an AttributeError.
# This also applies when you call an undefined method.
