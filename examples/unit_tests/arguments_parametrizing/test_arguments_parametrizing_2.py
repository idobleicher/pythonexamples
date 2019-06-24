#It is also possible to mark individual test instances within parametrize, for example with
# the builtin mark.xfail:
import pytest

@pytest.mark.parametrize(
    "test_input,expectedq",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval2(test_input, expected):
    assert eval(test_input) == expected

   #The one parameter set which caused a failure previously now shows up as an “xfailed (expected to fail)” test..