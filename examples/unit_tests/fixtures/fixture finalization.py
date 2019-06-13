# Fixture finalization / executing teardown code
# pytest supports execution of fixture specific finalization code when the fixture goes out of scope.
# By using a yield statement instead of return, all the code after the yield statement serves as the teardown code:

# content of conftest.py

import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection  # provide the fixture value
    print("teardown smtp")
    smtp_connection.close()
#The print and smtp.close() statements will execute when the last test in the module has finished execution, regardless of the exception status of the tests.

