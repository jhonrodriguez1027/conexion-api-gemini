# listar_modelos_completo.py
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

clave_api = os.getenv("GOOGLE_API_KEY")
cliente = genai.Client(api_key=clave_api)

print("📋 Modelos y sus capacidades:\n")
print("="*80)

for modelo in cliente.models.list():
    print(f"\n📌 Nombre: {modelo.name}")
    print(f"   Display Name: {modelo.display_name}")
    print(f"   Description: {modelo.description[:100] if modelo.description else 'N/A'}...")
    print(f"   Supported Methods: {modelo.supported_methods if hasattr(modelo, 'supported_methods') else 'No especificado'}")
    print("-"*80)