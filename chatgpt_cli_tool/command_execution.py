```python
import subprocess
from .utils import print_error, print_info
from .history import update_user_history

def execute_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        if process.returncode != 0:
            print_error(f"Error executing command: {error.decode().strip()}")
            return None

        return output.decode().strip()

    except Exception as e:
        print_error(f"Error executing command: {str(e)}")
        return None

def show_execution_menu(commands):
    print_info("Select a command to execute:")
    for i, command in enumerate(commands, start=1):
        print(f"{i}. {command}")

    choice = input("Enter your choice: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(commands):
        print_error("Invalid choice. Please try again.")
        return

    command = commands[int(choice) - 1]
    print_info(f"Executing command: {command}")
    output = execute_command(command)

    if output is not None:
        print_info("Command executed successfully. Output:")
        print(output)

        update_user_history(command, output)
    else:
        print_error("Command execution failed.")
```
