# https://www.geeksforgeeks.org/with-statement-in-python/
#
# Supporting the “with” statement in user defined objects

# There is nothing special in open() which makes it usable with the with statement and the same
#  functionality can be provided in user defined objects.
#
# Supporting with statement in your objects will ensure that you never leave any resource open.

# To use with statement in user defined objects you only need to add the
# methods __enter__() and __exit__() in the object methods.
#
# Consider the following example for further clarification.
#
#

#This is how we use the with statement with user defined objects.-

#This interface of __enter__() and __exit__() methods which provides the support of with statement in user defined objects is called Context Manager


# a simple file writer object


class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("this is enter")
        # resource descriptors- are the handles provided by the operating system to access the requested resources.
        # In the following code block, file is a descriptor of the file stream resource.
        self.file = open(self.file_name, 'w')
        return self.file


    # All the acquired resources are released in the __exit__() method.
    def __exit__(self, exc_type, exc_value, tb):
        print("this is exit")
        self.file.close()


# using with statement with MessageWriter

#what follows the with keyword is the constructor of MessageWriter

#The name xfile here is used to refer to the file descriptor returned by the __enter__() method
with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')

#this is enter
#this is exit

# As soon as the execution enters the context of the with statement a MessageWriter object is created
# and python then calls the __enter__() method.
# In this __enter__() method, initialize the resource you wish to use in the object.
#
# This __enter__() method should always return a descriptor of the acquired resource.




file = open('hello.txt')