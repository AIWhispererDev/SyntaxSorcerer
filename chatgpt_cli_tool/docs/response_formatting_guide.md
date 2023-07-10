# Response Formatting Guide

This guide will help you understand how the response formatting works in our ChatGPT CLI tool.

## Overview

The response formatting functionality is handled by the `response_formatting.py` module. This module is responsible for formatting the responses received from the ChatGPT API and printing them in a user-friendly manner on the terminal.

## Functions

### format_response

This function takes the raw response from the ChatGPT API and formats it for display. It uses the color configuration from the `config.py` file to colorize the output.

Usage:

```python
from response_formatting import format_response

formatted_response = format_response(raw_response)
```

### convert_to_ansi

This function takes a string and a color name as input and returns the string wrapped in ANSI escape sequences for the specified color. The color names are defined in the `config.py` file.

Usage:

```python
from response_formatting import convert_to_ansi

colored_string = convert_to_ansi('Hello, World!', 'green')
```

## Configuration

The color configuration for the response formatting is stored in the `config.py` file. You can modify the `COLOR_CONFIG` dictionary to change the colors used for different parts of the response.

Example:

```python
COLOR_CONFIG = {
    'question': 'blue',
    'answer': 'green',
    'error': 'red',
}
```

In this configuration, questions will be printed in blue, answers in green, and errors in red.

## Conclusion

The response formatting functionality is a crucial part of the ChatGPT CLI tool, as it ensures that the responses from the ChatGPT API are displayed in a readable and user-friendly manner. By understanding how this functionality works and how to configure it, you can customize the tool to suit your preferences.