from openai import OpenAI
from dotenv import load_dotenv, set_key, dotenv_values
import json

# Load environment variables from .env file
load_dotenv()
secret_key = (dotenv_values('.env'))["OPENAI_API_KEY"]
client = OpenAI(api_key=secret_key)

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
    

# FUNCTION: call gpt apit and return unformatted ouput
def get_GPT_unformat_output(message_history):
    api_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= message_history
    )
    
    content = api_response.choices[0].message.content
    
    # update message history
    update_msg_history("assistant", content)
    return content
    
# FUNCTION: send msgHistory.JSON to GPT_API and return 'content' from output
def get_GPT_content(filepath):
    with open(filepath, 'r') as file:
        chat_data = json.load(file)
        messages = chat_data['messages']
        
    output_content = get_GPT_unformat_output(messages)
    return output_content


# FUNCTION: Send user's prompt to GPT api, update message history, return 'content' from gptAPI
def user_to_gpt(prompt):
    update_msg_history("user", prompt)
    gpt_output = get_GPT_content("msgHistory.json")
    return gpt_output
    
    

# FUNCTION: get_Image() insert prompt and return image url
def get_image(prompt):
    #Parse the prompt
    
    response = client.images.generate(
        model="dall-e-3",
        prompt= prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    image_url = response.data[0].url
    return image_url


def process(prompt):
    res = user_to_gpt(prompt)
    im_url = get_image(res.split(",")[0])
    
    return [res, im_url]

def initialize():
    res = get_GPT_content("msgHistory.json")
    im_url = get_image(res.split(",")[0])
    
    return [res, im_url]