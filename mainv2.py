import os
import requests
import json

# URL de la API de DeepSeek
api_url = 'https://api.deepseek.com'

# Tu clave de API de DeepSeek
api_key = os.getenv('DEEPSEEK_API_KEY')

# Encabezados de la solicitud
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {'sk-57684f2249d24c27b6649c411db177f6'}'
}

# Datos de la solicitud
data = {
    'model': 'deepseek-v3',  # Especifica el modelo que deseas utilizar
    'prompt': 'Escribe un poema sobre la naturaleza en español.',
    'max_tokens': 150,       # Número máximo de tokens en la respuesta
    'temperature': 0.7       # Controla la aleatoriedad de la respuesta
}

# Realiza la solicitud POST a la API
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Analiza la respuesta JSON
    result = response.json()
    # Imprime el texto generado
    print(result['choices'][0]['text'])
else:
    # Imprime el código de estado y el mensaje de error
    print(f'Error {response.status_code}: {response.text}')
