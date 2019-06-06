#For ensuring that the mock objects in your tests have the same api as the objects they are replacing,
# you can use auto-speccing.
#
# Auto-speccing can be done through the autospec argument to patch,
# or the create_autospec() function.
# Auto-speccing creates mock objects
# that have the same attributes and methods as the objects they are replacing,
# and any functions and methods (including constructors) have the same call signature as the real object.

#This ensures that your mocks will fail in the same way as your production code if they are used incorrectly:

from unittest.mock import create_autospec
def function(a, b, c):
    pass

mock_function = create_autospec(function, return_value='fishy')
mock_function(1, 2, 3)
'fishy'

mock_function.assert_called_once_with(1, 2, 3)
#mock_function('wrong arguments')
#Traceback (most recent call last):