# ChatGPT CLI Tool

This is a command-line tool that utilizes the power of ChatGPT, bringing it straight to your terminal. You can ask questions and receive insightful responses related to shell scripting, making it an indispensable asset for both beginners and seasoned users alike. It interacts with an API to send questions and receive formatted responses. The API provides concise explanations and commands for Linux shell environments using ChatGPT as a backend. It maintains a configuration file, user history, shows the menu for executing returned commands, and formats response output with configurable colors converted to ANSI-escaped sequences.

## Installation

```bash
git clone https://github.com/yourusername/chatgpt_cli_tool.git
cd chatgpt_cli_tool
pip install -r requirements.txt
```

## Usage

To start the tool, run the following command:

```bash
python main.py
```

For detailed usage instructions, please refer to the [Usage Guide](docs/usage_guide.md).

## Configuration

The tool maintains a configuration file for API keys, API URLs, and color configurations. For detailed instructions on how to configure the tool, please refer to the [Configuration Guide](docs/configuration_guide.md).

## Command Execution

The tool provides a menu for executing returned commands. For detailed instructions on how to use this feature, please refer to the [Command Execution Guide](docs/command_execution_guide.md).

## Response Formatting

The tool formats response output with configurable colors converted to ANSI-escaped sequences. For detailed instructions on how to use this feature, please refer to the [Response Formatting Guide](docs/response_formatting_guide.md).

## User History

The tool maintains a user history of asked questions and received responses. For detailed instructions on how to use this feature, please refer to the [History Guide](docs/history_guide.md).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)