from getpass import getpass
import requests
from requests.auth import HTTPBasicAuth , AuthBase

user_url = 'https://api.github.com/user'
username = "username1"
# get pass open prompt
#password = getpass()

password = "pass1232"
#When you pass your username and password in a tuple to the auth parameter,
# requests is applying the credentials using HTTP’s Basic access authentication scheme under the hood

response = requests.get(user_url, auth=(username, password))
print(response.status_code)
#401 if not approved

#Therefore, you could make the same request by passing explicit Basic authentication credentials using HTTPBasicAuth:

requests.get(user_url , auth=HTTPBasicAuth(username, password) )


#Though you don’t need to be explicit for Basic authentication, you may
# want to authenticate using another method.
# requests provides other methods of authentication out of the box such as HTTPDigestAuth and HTTPProxyAuth.
#You can even supply your own authentication mechanism.
# To do so, you must first create a subclass of AuthBase. Then, you implement __call__():

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))






