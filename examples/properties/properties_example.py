
# Properties provide a way of customizing access to instance attributes.

# They are created by putting the property decorator above a method, which means when the
# instance attribute with the same name as the method is accessed, the method will be called instead.

# One common use of a property is to make an attribute read-only.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#False

#pizza.pineapple_allowed = True
#AttributeError: can't set attribute

class Person:
    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

person_young =  Person(5)
print(person_young.isAdult)
#false

person_old =  Person(20)
print(person_old.isAdult)
#true