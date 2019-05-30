#Inspecting Your Request
import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})

response.request.headers['Content-Type']
#'application/json'
response.request.url
#'https://httpbin.org/post'
response.request.body
#b'{"key": "value"}'
