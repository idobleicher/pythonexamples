from unittest.mock import patch
from examples.unit_tests.mock_examples import Foo



#Perform multiple patches in a single call.
# It takes the object to be patched (either as an object or a string to fetch the object by importing) and keyword arguments for the patches:

patched_object='examples.unit_tests.mock_examples.Foo'


with patch.multiple(patched_object,SOME_FIELD="y",SOME_FIELD2="z",SOME_FIELD3="q"):
    print(Foo.SOME_FIELD)
    print(Foo.SOME_FIELD2)
    print(Foo.SOME_FIELD3)





