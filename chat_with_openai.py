from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")

client = OpenAI(
  api_key = api_key
)

completion = client.chat.completions.create(
  model="gpt-4",
  store=True,
  messages=[
    {"role": "user", "content": "Hi there Dave here!"}
  ]
)

print(completion.choices[0].message)
