import requests

#Performance
#When using requests, especially in a production application environment,
# it’s important to consider performance implications.
# Features like timeout control, sessions, and retry limits can help you keep your application running smoothly.
requests.get('https://api.github.com', timeout=1)

#You can also pass a tuple to timeout with the first element being a connect
# timeout (the time it allows for the client to establish a connection to the server),
# and the second being a read timeout (the time it will wait on a response once your client has established a connection):
requests.get('https://api.github.com', timeout=(2, 5))

# If the request establishes a connection within 2 seconds and receives data within 5 seconds of the connection being established,
# then the response will be returned as it was before.
# If the request times out, then the function will raise a Timeout exception:

import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=0.1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')



