import requests
import requests_mock

#As a context manager:
with requests_mock.mock() as m:
    m.get(requests_mock.ANY, text="xxx")

    response = requests.get('http://test.com')
    print("text:", response.text)
    #text: xxx
    response = requests.get('http://xxc.com')
    print("text:", response.text)
    # text: xxx
