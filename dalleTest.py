from openai import OpenAI

OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(
  model="dall-e-3",
  prompt="a mighty chinese warrior king",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)