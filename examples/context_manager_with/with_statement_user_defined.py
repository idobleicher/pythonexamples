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

# a simple file writer object


class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()

        # using with statement with MessageWriter


with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')
