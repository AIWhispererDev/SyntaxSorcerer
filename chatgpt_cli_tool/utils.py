```python
import os
import json
from termcolor import colored

def print_error(message):
    print(colored(message, 'red'))

def print_info(message):
    print(colored(message, 'blue'))

def load_config():
    try:
        with open('config.py', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print_error('Configuration file not found. Please ensure config.py exists.')
        return None

def save_config(config):
    try:
        with open('config.py', 'w') as config_file:
            json.dump(config, config_file)
    except Exception as e:
        print_error(f'Error saving configuration: {e}')

def load_history():
    try:
        with open('history.py', 'r') as history_file:
            return json.load(history_file)
    except FileNotFoundError:
        print_info('No history found. A new history file will be created.')
        return []

def save_history(history):
    try:
        with open('history.py', 'w') as history_file:
            json.dump(history, history_file)
    except Exception as e:
        print_error(f'Error saving history: {e}')

def convert_to_ansi(color):
    color_mapping = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    return color_mapping.get(color, '\033[0m')
```