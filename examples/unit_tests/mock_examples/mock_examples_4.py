from unittest import mock
from unit_tests.mock_examples import Foo2
import pytest


@pytest.fixture(autouse=True)
def patch_my_method():
    with mock.patch("unit_tests.mock_examples.Foo2.my_method", new=mocked_function) :
        yield

def mocked_function():
    print ("in mocked function")
    return 2


def test_with_my_method(patch_my_method):
    result = Foo2.my_method()
    assert result == 2