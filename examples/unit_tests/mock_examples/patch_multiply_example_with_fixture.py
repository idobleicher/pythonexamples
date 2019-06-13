from unittest.mock import patch
from examples.unit_tests.mock_examples import Foo
import pytest


#Perform multiple patches in a single call.
# It takes the object to be patched (either as an object or a string to fetch the object by importing) and keyword arguments for the patches:

patched_object='examples.unit_tests.mock_examples.Foo'

@pytest.fixture(scope='module')
def fields_environment():
    with patch.multiple(patched_object,SOME_FIELD="y",SOME_FIELD2="y",SOME_FIELD3="y") as mock_fields:
        yield mock_fields

def test_1(fields_environment):
    assert Foo.SOME_FIELD == "y"

def test_1(fields_environment):
    assert Foo.SOME_FIELD2 == "y"

def test_1(fields_environment):
    assert Foo.SOME_FIELD3 == "y"