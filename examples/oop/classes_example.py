#This code defines a class named Cat, which has two attributes: color and legs.
#Then the class is used to create 3 separate objects of that class.

#method is like function but run on object

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)