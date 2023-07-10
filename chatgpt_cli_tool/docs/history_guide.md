# User History Guide

The user history functionality is an important part of the ChatGPT CLI tool. It allows you to keep track of the questions you've asked and the responses you've received. This guide will help you understand how to interact with the user history.

## Accessing User History

To access your user history, you can use the `get_user_history` function from the `history.py` module. This function does not require any arguments and returns a list of dictionaries, each containing a question and its corresponding response.

```python
from history import get_user_history

history = get_user_history()
```

Each item in the returned list is a dictionary with the following structure:

```python
{
    'question': 'Your question here',
    'response': 'ChatGPT response here'
}
```

## Updating User History

To update your user history with a new question and response, you can use the `update_user_history` function from the `history.py` module. This function requires two arguments: the question you asked and the response you received.

```python
from history import update_user_history

question = 'Your question here'
response = 'ChatGPT response here'

update_user_history(question, response)
```

This will add the question and response to your user history.

## Viewing User History

To view your user history in a user-friendly format, you can use the `print_user_history` function from the `utils.py` module. This function does not require any arguments.

```python
from utils import print_user_history

print_user_history()
```

This will print your user history to the terminal in a readable format.

Remember, the user history is an important tool for keeping track of your interactions with the ChatGPT CLI tool. Make sure to use it to its full potential!