# "leak" a file descriptor. Simply: by not closing opened files

files = []
for x in range(100000):
    files.append(open('foo.txt', 'w'))

    #You can get got an error message like the following:

    #Traceback (most recent call last):
#   File "test.py", line 3, in <module>
# OSError: [Errno 24] Too many open files: 'foo.txt'

    #Closing each file:


    for x in range(10000):
        f = open('foo.txt', 'w')
        f.close()
        files.append(f)

        #In real systems, it's difficult to make sure that close() is called on every file opened,
        # especially if the file is in a function that may raise an exception or has multiple return paths.

        #In other languages, developers are forced to use try...except...finally every time they work with a file (or any other type of resource
        # that needs to be closed, like sockets or database connections).
        # Pythonan gives us a simple way to make sure all resources we use are properly cleaned up,
        # regardless of if the code returns or an exception is thrown: context managers. - context manager