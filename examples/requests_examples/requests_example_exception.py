import requests
from requests.exceptions import HTTPError

#Let’s say you don’t want to check the response’s status code in an if statement.
# Instead, you want to raise an exception if the request was unsuccessful.
# You can do this using .raise_for_status():


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')