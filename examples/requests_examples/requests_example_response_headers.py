import requests



response = requests.get('https://api.github.com')

print(response.headers)
#{'Server': 'GitHub.com', 'Date': 'Thu, 30 May 2019 06:51:17 GMT', 'Content-Type': 'application/json; charset=utf-8',

print(response.headers['Content-Type'])
#application/json; charset=utf-8

#here is something special about this dictionary-like headers object, though.
# The HTTP spec defines headers to be case-insensitive,
# which means we are able to access these headers without worrying about their capitalization:

response.headers['content-type']
#'application/json; charset=utf-8'