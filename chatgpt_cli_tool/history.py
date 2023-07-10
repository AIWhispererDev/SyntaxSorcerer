```python
import os
import json

HISTORY_FILE = "user_history.json"

def get_user_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r') as file:
        return json.load(file)

def update_user_history(question, response):
    history = get_user_history()
    history.append({
        "question": question,
        "response": response
    })
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)
```