
# user_prompt = input ("Start upgrade")
# print(user_prompt)
import requests
from html.parser import HTMLParser

response = requests.get('http://visionbld:8080/view/Vision/job/Vision-4.10/lastSuccessfulBuild/artifact/')

response_body = response.text
#print(response_body)
# pattern = re.compile('Vision-4.10\s*#(\d+)\s+', re.IGNORECASE)
# match = pattern.match(response_body)
HTMLParser.feed( response_body)



