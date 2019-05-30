#The response of a GET request often has some valuable information, known as a payload, in the message body.
# Using the attributes and methods of Response, you can view the payload in a variety of different formats.

#To see the response’s content in bytes, you use .content:

import requests



response = requests.get('https://api.github.com')
print(response.content)



#b'{"current_user_url":"https://api.github ...and etc

#While .content gives you access to the raw bytes of the response payload, you will often want to convert them into a string using a
# character encoding such as UTF-8. response will do that for you when you access .text:

print(response.text)
#"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url": and etc

#Because the decoding of bytes to a str requires an encoding scheme, requests will try to guess the encoding based on
# the response’s headers if you do not specify one.
# You can provide an explicit encoding by setting .encoding before accessing .text:

response.encoding = 'utf-8' # Optional: requests infers this internally
print(response.text)
#'{"current_user_url": and etc

# If you take a look at the response, you’ll see that it is actually serialized JSON content.
# To get a dictionary, you could take the str you retrieved from .text
# and deserialize it using json.loads().
# However, a simpler way to accomplish this task is to use .json():
print(response.json())
#{'current_user_url': 'https://api.github.com/user', 'cur  and etc
