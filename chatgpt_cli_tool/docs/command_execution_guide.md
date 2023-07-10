# Command Execution Guide

This guide will help you understand how the command execution functionality works in the ChatGPT CLI tool.

## Overview

The command execution functionality is primarily handled by the `command_execution.py` module. This module interacts with the shell environment to execute the commands returned by the ChatGPT model.

## Functions

### execute_command

This function takes a command string as an argument and executes it in the shell environment. It returns the output of the command execution.

```python
def execute_command(command):
    # implementation
```

### show_execution_menu

This function displays a menu to the user with the option to execute the returned command. It takes the command string as an argument.

```python
def show_execution_menu(command):
    # implementation
```

## Usage

To use the command execution functionality, you need to import the `command_execution.py` module and call the appropriate function.

Here is an example of how to use the `execute_command` function:

```python
from command_execution import execute_command

command = "ls -l"
output = execute_command(command)
print(output)
```

And here is an example of how to use the `show_execution_menu` function:

```python
from command_execution import show_execution_menu

command = "ls -l"
show_execution_menu(command)
```

Remember to handle any exceptions that may occur during command execution. The `execute_command` function may raise a `CommandExecutionError` if there is an error during command execution.

## Conclusion

The command execution functionality is a crucial part of the ChatGPT CLI tool. It allows users to execute the commands returned by the ChatGPT model directly from the tool, making it a powerful asset for both beginners and seasoned users alike.