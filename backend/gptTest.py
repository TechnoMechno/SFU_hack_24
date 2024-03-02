from openai import OpenAI
from dotenv import load_dotenv, set_key, dotenv_values
import os

# Load environment variables from .env file
load_dotenv()
secret_key = (dotenv_values('.env'))["OPENAI_API_KEY"]
client = OpenAI(api_key=secret_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(completion.choices[0].message)


