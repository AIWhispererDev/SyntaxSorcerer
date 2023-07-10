# Configuration Guide

This guide will help you understand how to configure the ChatGPT CLI tool.

## Configuration File

The configuration file for the ChatGPT CLI tool is `config.py`. This file contains several important variables that control the behavior of the tool.

### API_KEY

This is the API key for the ChatGPT API. You need to replace the placeholder with your actual API key.

```python
API_KEY = "your-api-key"
```

### API_URL

This is the URL of the ChatGPT API. The default value is set to the official OpenAI API.

```python
API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions"
```

### COLOR_CONFIG

This is the configuration for the color output of the tool. It is a dictionary where the keys are the types of output (e.g., "info", "error") and the values are the corresponding ANSI color codes.

```python
COLOR_CONFIG = {
    "info": "\033[94m",  # Blue
    "error": "\033[91m",  # Red
    "default": "\033[0m",  # Reset
}
```

## Updating Configuration

To update the configuration, simply open the `config.py` file in a text editor and modify the values as needed. After saving the changes, they will take effect the next time you run the ChatGPT CLI tool.

## Next Steps

After configuring the tool, you can start using it by running `main.py`. For more information on how to use the tool, refer to the `usage_guide.md`. If you encounter any issues, check the `error` output in your terminal and refer to the `command_execution_guide.md` and `response_formatting_guide.md` for troubleshooting.