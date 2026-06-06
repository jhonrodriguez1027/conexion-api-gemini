
# 🤖 Conexión a Gemini API


Este proyecto implementa una conexión básica a la API de Google Gemini utilizando Python. El objetivo es validar la configuración del entorno de desarrollo, verificar la conectividad a Internet y realizar una consulta a un modelo de inteligencia artificial mediante la API de Gemini.Script en Python para conectar y probar la API de Google Gemini, mostrando cómo interactuar con modelos de lenguaje avanzados.



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
```
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

📋 Requisitos Previos
Python 3.8 o superior.

Una cuenta de Google para acceder a las herramientas de desarrollo.

Una API Key de Gemini (puedes obtenerla de forma gratuita).

🔑 Cómo obtener tu API Key
Dirígete a Google AI Studio.

Inicia sesión con tu cuenta de Google.

Haz clic en el botón "Get API Key" (Obtener clave de API).

Crea una nueva clave para un proyecto nuevo o existente y cópiala.

🚀 Instalación y Configuración
Sigue estos pasos en tu terminal (PowerShell o CMD) para clonar, configurar y ejecutar el proyecto localmente.

1. Clonar el repositorio y navegar a la carpeta
PowerShell
git clone [https://github.com/jhonrodriguez1027/conexion-api-gemini.git](https://github.com/jhonrodriguez1027/conexion-api-gemini.git)
cd conexion-api-gemini
2. Crear y activar el entorno virtual
PowerShell
# Crear el entorno virtual llamado '.venv'
python -m venv .venv

# Activar el entorno virtual en Windows (PowerShell)
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .\.venv\Scripts\Activate.ps1)
3. Instalar las dependencias del proyecto
PowerShell
pip install -r requeriments.txt
4. Configurar las Variables de Entorno
Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que tus scripts de Python) y agrega tu clave de la siguiente manera:

Plaintext
GEMINI_API_KEY=tu_clave_api_aqui
⚠️ Importante: Reemplaza tu_clave_api_aqui por el token real que copiaste de Google AI Studio. Asegúrate de no dejar espacios en blanco ni usar comillas. Gracias al archivo .gitignore, esta clave permanecerá segura en tu máquina local.


<img width="1178" height="195" alt="Captura de pantalla 2026-06-06 100246" src="https://github.com/user-attachments/assets/bf867d16-9cc4-4881-a79e-30093e32c3b3" />


<img width="1252" height="196" alt="REPORT" src="https://github.com/user-attachments/assets/4cb719f2-050b-4787-aafd-bf13cb355b5c" />
### 1. Clonar el repositorio

```bash
git clone https://github.com/jhonrodriguez1027/conexion-api-gemini.git
cd gemini-conexion
