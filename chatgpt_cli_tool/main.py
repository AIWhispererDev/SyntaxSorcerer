```python
import argparse
from api_interaction import send_question, receive_response
from command_execution import execute_command, show_execution_menu
from response_formatting import format_response, convert_to_ansi
from config import API_KEY, API_URL, COLOR_CONFIG
from history import get_user_history, update_user_history
from utils import print_error, print_info

def main():
    parser = argparse.ArgumentParser(description='ChatGPT CLI Tool')
    parser.add_argument('question', type=str, help='Question related to shell scripting')
    args = parser.parse_args()

    try:
        print_info("Sending question to ChatGPT...")
        send_question(API_URL, API_KEY, args.question)
        response = receive_response(API_URL, API_KEY)

        if response:
            print_info("Received response from ChatGPT.")
            formatted_response = format_response(response, COLOR_CONFIG)
            print_info("Formatted response:")
            print(formatted_response)

            print_info("Updating user history...")
            update_user_history(args.question, response)

            print_info("Showing execution menu...")
            command = show_execution_menu(response)
            if command:
                print_info("Executing command...")
                execute_command(command)
            else:
                print_info("No command selected for execution.")
        else:
            print_error("No response received from ChatGPT.")
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```