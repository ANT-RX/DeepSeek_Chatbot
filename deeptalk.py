import os
from openai import OpenAI
from dotenv import load_dotenv
from .include import chat

# Cargamos las claves de acceso de la API
load_dotenv()
DeepSeek_Key = os.getenv('DEEPSEEK_API_KEY')

# Crea un cliente con el url de la API y la clave de la API
client = OpenAI(api_key=DeepSeek_Key, base_url="https://api.deepseek.com")

sys_prompt = "Eres un asistente amable."
max_tok = 100

try:
    usr_prompt = input("Type your answer:")
    chat(client, sys_prompt, usr_prompt, max_tok)
    print(chat.answer)
except ValueError as e:
    print(f'Error ocurrido: {e}')