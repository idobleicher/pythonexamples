from unittest.mock import Mock , MagicMock , patch
from examples.unit_tests.mock_examples import Foo
##########from examples.unit_tests.mock_examples.Foo import FooCls

#Common uses for Mock objects include:
#
# Patching methods
# Recording method calls on objects

#You might want to replace a method on an object to check that it is called with the correct arguments by another part of the system:

#>>> real = SomeClass()
# >>> real.method = MagicMock(name='method')
# >>> real.method(3, 4, 5, key='value')
# <MagicMock name='method()' id='...'>


class ProductionClass:

    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass

#In this example we patched a method directly on an object to check that it was called correctly
real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3)


#nother common use case is to pass an object into a method (or some part of the system under test)
# and then check that it is used in the correct way.


class ProductionClass2:
    def closer(self, something):
        something.close()

real = ProductionClass2()
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()

#Mocking Classes
#A common use case is to mock out classes instantiated by your code under test

#In the example below we have a function some_function that instantiates Foo and calls a method on it.
# The call to patch() replaces the class Foo with a mock.
# The Foo instance is the result of calling the mock, so it is configured by modifying the mock return_value.



def some_function():
    instance = Foo.FooCls()
    #will not work !!!instance = FooCls()
    return instance.somemethod()


with patch('examples.unit_tests.mock_examples.Foo.FooCls') as MockHelper:
    instance1 = MockHelper.return_value
    instance1.somemethod.return_value = 'the result'

    result = some_function()
    assert result == 'the result'