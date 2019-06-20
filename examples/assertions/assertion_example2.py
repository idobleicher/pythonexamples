# The assert can take a second argument that is passed to the AssertionError
# raised if the assertion fails.


temp = -10
assert (temp >= 0), "Colder than absolute zero!"

# AssertionError: Colder than absolute zero!

# AssertionError exceptions can be caught and handled like any other exception using the try-except statement,
#  but if not handled, this type of exception will terminate the program.
