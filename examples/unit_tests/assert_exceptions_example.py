import re
import pytest

err_msg = "Invalid email format"

def check_email_format(email):
    """check that the entered email format is correct"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception(err_msg)
    else:
        return "Email format is ok"

def test_email_exception():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception) as e:
        assert check_email_format("bademailformat.com")
    assert str(e.value) == err_msg