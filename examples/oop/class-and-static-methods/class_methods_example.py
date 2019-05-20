
#Methods of objects we've looked at so far are called by an instance of a class,
#  which is then passed to the self parameter of the method.

#Class methods are different - they are called by a class, which is passed to the
# cls parameter of the method.

#A common use of these are factory methods, which instantiate an instance of a class,
# using different parameters than those usually passed to the class constructor.

#Class methods are marked with a classmethod decorator.

#Technically, the parameters self and cls are just conventions;
# they could be changed to anything else.
#  However, they are universally followed, so it is wise to stick to using them.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    # new_square is a class method and is called on the class, rather than on an
    # instance of the class. It returns a new object of the class cls.
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)

print(square.calculate_area())
#25