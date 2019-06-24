from unittest import mock
from unit_tests.mock_examples import Foo2


def mocked_function():
    print ("in mocked function")
    return 2


print(Foo2.my_method())

with mock.patch("unit_tests.mock_examples.Foo2.my_method" , new=mocked_function) as MockHelper:
    result = Foo2.my_method()
    assert result == 2