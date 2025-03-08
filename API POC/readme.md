# API de Análisis de Transcripciones

Esta API, desarrollada con FastAPI, permite analizar transcripciones de reuniones para generar requerimientos técnicos detallados. Utiliza el modelo GPT-4 de OpenAI para procesar el texto y devolver un conjunto estructurado de requerimientos en formato JSON.

## Características

- **Descripción del Requerimiento**: Resume el objetivo del proyecto en términos claros.
- **Tareas Técnicas**: Desglosa las actividades necesarias para implementar la solución.
- **Estimación de Tiempos**: Asigna tiempos aproximados a cada tarea en días.
- **Roles Requeridos**: Identifica los perfiles (ej., backend, frontend, DevOps) involucrados.

## Requisitos Previos

- Python 3.7 o superior
- Clave de API de OpenAI

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn openai
   ```

3. Configura la clave de API de OpenAI como una variable de entorno:

   ```bash
   export OPENAI_API_KEY='tu_clave_de_api'
   ```

   En Windows, usa:

   ```cmd
   set OPENAI_API_KEY=tu_clave_de_api
   ```

## Ejecución

Para iniciar el servidor de la API, ejecuta el siguiente comando:
