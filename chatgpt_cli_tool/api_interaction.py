```python
import requests
from .config import API_KEY, API_URL
from .utils import print_error

def send_question(question):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'question': question
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print_error(f"HTTP error occurred: {err}")
    except Exception as err:
        print_error(f"An error occurred: {err}")

def receive_response(response):
    if response and 'answers' in response:
        return response['answers']
    else:
        print_error("No response received from the API.")
        return None
```