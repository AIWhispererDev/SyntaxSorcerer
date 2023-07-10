```python
import os
import json

# Configuration file path
CONFIG_FILE_PATH = "config.json"

# Default configuration
DEFAULT_CONFIG = {
    "API_KEY": "",
    "API_URL": "https://api.openai.com/v1/engines/davinci-codex/completions",
    "COLOR_CONFIG": {
        "question": "\033[1;34m",  # Blue
        "response": "\033[1;32m",  # Green
        "error": "\033[1;31m",  # Red
        "info": "\033[1;33m"  # Yellow
    }
}

def load_config():
    """
    Load the configuration from the config file.
    If the file does not exist, create it with the default configuration.
    """
    if not os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(DEFAULT_CONFIG, config_file)
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config = json.load(config_file)
    return config

def update_config(new_config):
    """
    Update the configuration file with the new configuration.
    """
    with open(CONFIG_FILE_PATH, 'w') as config_file:
        json.dump(new_config, config_file)

# Load the configuration when the module is imported
CONFIG = load_config()
```