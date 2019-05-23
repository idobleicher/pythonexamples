# The contextlib module
#
# A class based context manager as shown in  with_statement_user_defined.py
# is not the only way to support the with statement in user defined objects.
#
# The contextlib module provides a few more abstractions built upon the basic context manager interface.
#
# Here is how we can rewrite the context manager for the MessageWriter object using the contextlib module.

from contextlib import contextmanager

class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename
        print("this is init of MessageWriter")

    # This part of code which appears The @contextmanager here is a decorator.
    # When this open_file() function is called, it creates a resource descriptor named file.
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            # because of the yield statement in its definition, the function open_file() is a generator function
            # This resource descriptor is then passed to the caller and is represented here by the variable my_file
            print("before yield file")
            # The code after the yield statement releases the acquired resources.
            yield file
        finally:
            print("before close")
            file.close()

# usage
#. After the code inside the with block is executed the program control returns back to the open_file() function
message_writer = MessageWriter('hello.txt')

print("before open file")
with message_writer.open_file() as my_file:
    #print("brfore write")
    my_file.write('hello world')

print("after open file")

# this is init of MessageWriter
# before open file
# before yield file
# before close
# after open file

# . The open_file() function resumes its execution and executes the code following the yield statement.


#
# The previous class-based implementation (with_statement_user_defined.py) and this generator-based implementation of context
# managers is internally the same.

# While the later seems more readable, it requires the knowledge of generators, decorators and yield.