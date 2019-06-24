#Parametrizing fixtures
#Fixture functions can be parametrized in which case they will be called multiple times,
# each time executing the set of dependent tests, i. e. the tests that depend on this fixture. Test functions usually do not need to be aware of their re-running. Fixture parametrization helps to write exhaustive functional tests for components which themselves can be configured in multiple ways.

#Extending the previous example, we can flag the fixture to create two smtp_connection fixture
# instances which will cause all tests using the fixture to run twice.
# The fixture function gets access to each parameter through the special request object:

# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing %s" % smtp_connection)
    smtp_connection.close()