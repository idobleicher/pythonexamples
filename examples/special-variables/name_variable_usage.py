#When the Python interpeter reads a source file, it first defines a few special variables.
# In this case, we care about the __name__ variable.

#When Your Module Is the Main Program
# If you are running your module (the source file) as the main program, e.g.python foo.py
# the interpreter will assign the hard-coded string "__main__" to the __name__ variable, i.e.

# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
#__name__ = "__main__"


# When Your Module Is Imported By Another
#
# On the other hand, suppose some other module is the main program and it imports your module.
# This means there's a statement like this in the main program, or in some other module the main program imports:

# Suppose this is in some other main program.
#import foo
#In this case, the interpreter will look at the filename of your module, foo.py,
# strip off the .py, and assign that string to your module's __name__ variable, i.e.

# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
#__name__ = "foo"

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()

print("after __name__ guard")

# before import
# before functionA
# before functionB
# before __name__ guard
# Function A
# Function B 10.0
# after __name__ guard