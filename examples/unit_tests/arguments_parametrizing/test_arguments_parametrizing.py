# pytest enables test parametrization at several levels:
#
# - pytest.fixture() allows one to parametrize fixture functions.
#
# - @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.
#
# - pytest_generate_tests allows one to define custom parametrization schemes or extensions.

#The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.
# Here is a typical example of a test function that implements checking that a certain input leads to an expected output:

import pytest

@pytest.mark.parametrize("test_input , expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    #AssertionError:
   # assert 54 == 42





