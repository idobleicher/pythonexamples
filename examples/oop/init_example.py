#The __init__ method is the most important method in a class.
#This is called when an instance (object) of the class is created, using the class name as a function.(like java constructor)

# All methods must have self as their first parameter, although it is not explicitly passed,
# Python adds the self argument  to the list for you;
# you do not need to include it when you call the methods.
# Within a method definition, self refers to the instance calling the method.

# Instances of a class have attributes, which are pieces of data associated with them.

# In this example, Cat instances have attributes color and legs.
# These can be accessed by putting a dot, and the attribute name after an instance.

# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
# ginger