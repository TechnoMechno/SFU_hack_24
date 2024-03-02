from openai import OpenAI
import json

OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

#GPT_handler

# FUNCTION: update_msg_history() Void Function to insert input from either asssitant or user to msgHistory Json file
def update_msg_history(role, input):
    
    if role == "user":
        # Read the file to store as 'data'
        with open("msgHistory.json", 'r') as file:
            history = json.load(file)
        new_message = {
        "role": "user",
        "content": input
        }
        history['messages'].append(new_message)
        
        # Write to the file
        with open("msgHistory.json", 'w') as file:
            json.dump(history, file, indent=4)
    elif role == "assistant":
         # Read the file to store as 'data'
        with open("msgHistory.json", 'r') as file:
            history = json.load(file)
        new_message = {
        "role": "assistant",
        "content": input
        }
        history['messages'].append(new_message)
        
        # Write to the file
        with open("msgHistory.json", 'w') as file:
            json.dump(history, file, indent=4)


# FUNCTION: get_GPT() Function to send msgHistory.JSON to GPT_API and return string outputted by API

    

# FUNCTION: get_Image() insert prompt and return image url

