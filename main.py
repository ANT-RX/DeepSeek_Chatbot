import os
from include import chat
from include import microphone
from openai import OpenAI
from dotenv import load_dotenv
import speech_recognition as sr

channel_data = 0

# Cargamos las claves de acceso de la API
load_dotenv()
DeepSeek_Key = os.getenv('DEEPSEEK_API_KEY')

# Crea un cliente con el url de la API y la clave de la API
client = OpenAI(api_key=DeepSeek_Key, base_url="https://api.deepseek.com")

sys_prompt = "Eres un asistente personal."
max_tok = 200

try:
    channel_data = int(input("Tipo de entrada: \n[Chat de voz][1] \n[Chat de texto][2] \n>>"))
    if channel_data == 1:
        microphone = microphone()
        usr_prompt = microphone.listen()
        print(f">> {usr_prompt}")
    else:
        usr_prompt = input("Type your answer:")

    chat_instance = chat(client, sys_prompt, usr_prompt, max_tok)
    chat_response = chat_instance.answer()
    print(chat_response.choices[0].message.content)
except ValueError as e:
    print(f'Error ocurrido: {e}')