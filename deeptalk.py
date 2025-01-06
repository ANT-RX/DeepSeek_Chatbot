# Please install OpenAI SDK first: `pip3 install openai`
from os import getenv
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DeepSeek_Key = getenv('DEEPSEEK_API_KEY')

client = OpenAI(api_key=DeepSeek_Key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Podrías traducir el siguiente texto inglés: Tengo que ir a dormir, sin embargo, debo terminar las pruebas de la API"},
    ],
    stream=False,
    max_tokens=300
)

print(response.choices[0].message.content)