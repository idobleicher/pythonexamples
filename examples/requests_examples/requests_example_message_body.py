import requests

response = requests.post('https://httpbin.org/post', data={'key':'value'})
print(response)
#<Response [200]>

response =  requests.post('https://httpbin.org/post', data=[('key', 'value')])
print(response)

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])

print(json_response['headers']['Content-Type'])