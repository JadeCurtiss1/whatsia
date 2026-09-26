import os
from google import genai
from dotenv import load_dotenv

# 1. Carga las variables desde el archivo .env
load_dotenv()

# 2. Inicializa el cliente (detecta automáticamente GOOGLE_GENERATIVE_AI_API_KEY)
client = genai.Client()

# 3. Prueba rápida con el modelo actualizado
try:
    response = client.models.generate_content(
        model='gemini-3.6-flash',  # <--- CAMBIADO AQUÍ
        contents='Di "¡Hola mundo desde Gemini 3.6!" en una oración corta.',
    )
    print("Respuesta de Gemini:")
    print(response.text)
    
except Exception as e:
    print("Ocurrió un error de autenticación o conexión:")
    print(e)
