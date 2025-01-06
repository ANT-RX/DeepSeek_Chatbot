import os
from deepseek import DeepSeekAPI

deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
# Inicializa el cliente de la API
api_client = DeepSeekAPI(api_key='sk-57684f2249d24c27b6649c411db177f6')

# Realiza una solicitud de finalización de chat
response = api_client.chat_completion(prompt='¡Hola!')
print(response)
