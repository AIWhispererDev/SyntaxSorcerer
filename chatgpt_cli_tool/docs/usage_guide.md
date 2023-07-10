# Usage Guide for ChatGPT CLI Tool

This guide will help you understand how to use the ChatGPT CLI tool.

## Installation

Before you can use the ChatGPT CLI tool, you need to install it. Here are the steps:

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/chatgpt_cli_tool.git
    ```

2. Navigate to the project directory:
    ```
    cd chatgpt_cli_tool
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Configuration

Before you start using the tool, you need to set up the configuration. You can do this by editing the `config.py` file. For more details, refer to the [Configuration Guide](./configuration_guide.md).

## Running the Tool

To run the tool, use the following command:

```
python main.py
```

You will be prompted to enter a question related to shell scripting. The tool will then interact with the API to send your question and receive a response. The response will be formatted according to your configuration settings and printed to the terminal.

## Executing Commands

If the response includes a shell command, you will be shown a menu to execute the command directly from the tool. For more details, refer to the [Command Execution Guide](./command_execution_guide.md).

## Viewing User History

You can view your history of questions and responses by accessing the user history. For more details, refer to the [History Guide](./history_guide.md).

## Formatting Responses

You can customize the formatting of the responses by editing the configuration file. For more details, refer to the [Response Formatting Guide](./response_formatting_guide.md).

## Troubleshooting

If you encounter any issues while using the tool, refer to the `print_error` and `print_info` functions in the `utils.py` file for debugging information.

Remember, this tool is powered by ChatGPT and is designed to help you with shell scripting questions. Enjoy using it!