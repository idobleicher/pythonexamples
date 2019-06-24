import pytest


class MyException(Exception):
    def __init__(self, message, some_param):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.some_param = some_param

def test_raises():
    with pytest.raises(MyException) as excinfo:
        raise MyException('some info' ,3)
    assert excinfo.value.args[0] == 'some info'
    assert excinfo.value.some_param == 3
