import requests

#Performance
#When using requests, especially in a production application environment,
# it’s important to consider performance implications.
# Features like timeout control, sessions, and retry limits can help you keep your application running smoothly.
requests.get('https://api.github.com', timeout=1)

#You can also pass a tuple to timeout with the first element being a connect
# timeout (the time it allows for the client to establish a connection to the server),
# and the second being a read timeout (the time it will wait on a response once your client has established a connection):


