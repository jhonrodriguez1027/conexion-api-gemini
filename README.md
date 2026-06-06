
# 🤖 Conexión a Gemini API


Este proyecto implementa una conexión básica a la API de Google Gemini utilizando Python. El objetivo es validar la configuración del entorno de desarrollo, verificar la conectividad a Internet y realizar una consulta a un modelo de inteligencia artificial mediante la API de Gemini.Script en Python para conectar y probar la API de Google Gemini, mostrando cómo interactuar con modelos de lenguaje avanzados.

# 🤖 Conexión a la API de Gemini

Este proyecto implementa una conexión básica y funcional a la API de Google Gemini utilizando Python. Su objetivo principal es validar la configuración del entorno de desarrollo, verificar la conectividad y realizar consultas iniciales a los modelos de lenguaje avanzados de Google.

---

## 📁 Estructura del Proyecto

```text
conexion-api-gemini/
│
├── .env                  # Variables de entorno (Clave API - Ignorado por Git)
├── .gitignore            # Archivos y carpetas excluidos de Git
├── README.md             # Documentación del proyecto
├── app.gemini.py         # Script principal de interacción con Gemini
├── lista_modelos.py      # Script para listar los modelos disponibles
├── prueba_entorno.py     # Script de validación de variables y conexión
└── requeriments.txt      # Dependencias del proyecto
## 📋 Requisitos Previos

- Python 3.8 o superior
- Cuenta de Google Cloud
- API Key de Gemini (gratuita)
-
-estructura del proyecto
  - Gemini-API/
  │
  ├── app_gemini.py
  ├── prueba_entornno.py
  ├── requirements.txt
  ├── .env
  ├── .gitignore
  ├── README.md


## 🔑 Obtener una API Key

1. Ve a [Google AI Studio](https://aistudio.google.com/)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Get API Key"
4. Crea una nueva clave y cópiala

## 🚀 Instalación y Ejecución
 Crear y activar entorno virtual
 python -m venv venv
venv\Scripts\activate

Instalar dependencias
  pip install -r requirements.txt 

  
#Configurar la API Key
Crea un archivo llamado .env en la raíz del proyecto (junto a app.py).
Abre el archivo con bloc de notas y escribe exactamente (sin comillas):

GOOGLE_API_KEY=tu_clave_api_aqui
Importante: Reemplaza tu_clave_api_aqui por la clave que copiaste.



<img width="1178" height="195" alt="Captura de pantalla 2026-06-06 100246" src="https://github.com/user-attachments/assets/bf867d16-9cc4-4881-a79e-30093e32c3b3" />


<img width="1252" height="196" alt="REPORT" src="https://github.com/user-attachments/assets/4cb719f2-050b-4787-aafd-bf13cb355b5c" />
### 1. Clonar el repositorio

```bash
git clone https://github.com/jhonrodriguez1027/conexion-api-gemini.git
cd gemini-conexion
