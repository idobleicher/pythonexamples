import requests

#SSL Certificate Verification
#Any time the data you are trying to send or receive is sensitive, security is important.
# The way that you communicate with secure sites over HTTP is by establishing an encrypted connection using SSL,
# which means that verifying the target server’s SSL Certificate is critical.

#The good news is that requests does this for you by default.
# However, there are some cases where you might want to change this behavior.

#If you want to disable SSL Certificate verification, you pass False to the verify parameter of the request function

requests.get('https://api.github.com', verify=False)

#Note: requests uses a package called certifi to provide Certificate Authorities.
# This lets requests know which authorities it can trust.
# Therefore, you should update certifi frequently to keep your connections as secure as possible.

