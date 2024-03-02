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
    

# FUNCTION: call gpt apit and return its output
def call_GPT(message_history):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= message_history
    )
    # Create dict to format api's response
    formatted_response = {
        "role": "assistant",
        "content": response.choices[0].message
    }
    
    return formatted_response
    
# FUNCTION: send msgHistory.JSON to GPT_API and return its output
def get_GPT_output(filepath):
    messages
    with open(filepath, 'r') as file:
        chat_data = json.load(file)
        messages = chat_data['messages']
        
    output_array = call_GPT(messages)
    
    # update message history
    

# FUNCTION: get_Image() insert prompt and return image url

