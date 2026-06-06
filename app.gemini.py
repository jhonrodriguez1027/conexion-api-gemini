# app.gemini.py - Versión robusta
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

clave_api = os.getenv("GOOGLE_API_KEY")

if not clave_api:
    print("❌ Error: No se encontró GOOGLE_API_KEY")
    exit(1)

cliente = genai.Client(api_key=clave_api)

print("✅ Cliente de Gemini inicializado correctamente")
print("🤖 Buscando modelo disponible...\n")

# Lista de modelos estándar que funcionan para texto
modelos_texto = [
    "models/gemini-2.0-flash-lite-001",
    "models/gemini-2.0-flash-lite",
    "models/gemini-flash-latest", 
    "models/gemini-pro-latest",
    "models/gemini-3.5-flash",
    "models/gemini-3-flash-preview",
    "models/gemini-3.1-flash-lite"
]

for modelo in modelos_texto:
    try:
        print(f"🔄 Probando: {modelo}")
        respuesta = cliente.models.generate_content(
            model=modelo,
            contents="Preséntate como experto en Machine Learning y responde: ¿Cuáles son las mejores prácticas para trabajar con GPT?"
        )
        
        print(f"\n✅ ¡ÉXITO! Usando modelo: {modelo}")
        print("\n" + "="*60)
        print("📝 RESPUESTA DE GEMINI:")
        print("="*60)
        print(respuesta.text)
        print("="*60)
        break  # Salir del bucle al primer éxito
        
    except Exception as e:
        print(f"⚠️ {modelo} falló: {str(e)[:80]}")
        continue