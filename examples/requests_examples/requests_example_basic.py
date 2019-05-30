import requests

url='https://api.github.com'
response = requests.get(url)

print(response.status_code)
#200

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

#equests goes one step further in simplifying this process for you.
# If you use a Response instance in a conditional expression,
# it will evaluate to True if the status code was between 200 and 400,
# and False otherwise.

if response:
    print('Success!')
else:
    print('An error has occurred.')

#Technical Detail: This Truth Value Test is made possible because __bool__() is an overloaded method on Response.

#This means that the default behavior of Response has been redefined to take the status code into account when
# determining the truth value of the object.



