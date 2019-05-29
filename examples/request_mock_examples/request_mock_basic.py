import requests
import requests_mock

mock_url='mock://test.com'
session = requests.Session()
adapter = requests_mock.Adapter()
session.mount('mock', adapter)

adapter.register_uri('GET', mock_url, text='data')
resp = session.get(mock_url)
print("code:" ,resp.status_code," response text:" , resp.text)
#code: 200  response text: data




print("------------------")
#As a context manager:
with requests_mock.mock() as reqmock:
    reqmock.get('http://test.com', text='data')
    response = requests.get('http://test.com')
    print ("text:" , response.text)
#text: data

print("------------------")
#as a decorator:
@requests_mock.mock()
def test_func(reqmock1):
    reqmock1.get('http://test.com', text='data')
    return requests.get('http://test.com').text

restext=test_func()
print("restext:" , restext)
#restext: data