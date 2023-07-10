```python
import json
from termcolor import colored
from .config import COLOR_CONFIG

def format_response(response):
    """
    Formats the response received from the API.
    """
    formatted_response = json.loads(response)
    return formatted_response

def convert_to_ansi(formatted_response):
    """
    Converts the formatted response to ANSI-escaped sequences.
    """
    ansi_response = ""
    for key, value in formatted_response.items():
        if key in COLOR_CONFIG:
            ansi_response += colored(value, COLOR_CONFIG[key])
        else:
            ansi_response += value
    return ansi_response

def print_formatted_response(response):
    """
    Prints the formatted response.
    """
    formatted_response = format_response(response)
    ansi_response = convert_to_ansi(formatted_response)
    print(ansi_response)
```