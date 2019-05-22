#https://www.geeksforgeeks.org/with-statement-in-python/

# with statement in Python is used in exception handling to make the code cleaner and much more readable.
# It simplifies the management of common resources like file streams.

# Observe the following code example on how the use of with statement makes code cleaner.
# file handling


#without using with statement
file = open('file_path', 'w')
try:
	file.write('hello world')
finally:
	file.close()


# Notice that unlike the first  implementation, there is no need to call file.close() when using with statement.
# The with statement itself ensures proper acquisition and release of resources.

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')



#
#  using the with statement makes the code compact and much more readable. T
#  hus, with statement helps avoiding bugs and leaks by ensuring that a resource is properly released when
#  the code using the resource is completely executed.
#
#  The with statement is popularly used with file streams, as shown above and with Locks, sockets, subprocesses and telnets etc.

























