from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
import os
import json
app = FastAPI()

# Inicializa el cliente de OpenAI con tu API Key
#openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt base para generar los requerimientos técnicos
PROMPT_TEMPLATE = """
Eres un experto en arquitectura de software y gestión de proyectos. 
Recibirás la transcripción de una reunión para levantar un requerimiento técnico.
Tu objetivo es analizar la transcripción y generar los siguientes elementos:

1. **Descripción del Requerimiento**: Resume el objetivo del proyecto en términos claros.
2. **Tareas Técnicas**: Desglosa las actividades necesarias para implementar la solución.
3. **Estimación de Tiempos**: Asigna tiempos aproximados a cada tarea en días.
4. **Roles Requeridos**: Identifica los perfiles (ej., backend, frontend, DevOps) involucrados.

Formato de salida JSON:
{{
  "descripcion": "...",
  "tareas": [
    {{"nombre": "...", "descripcion": "...", "tiempo_estimado": "...", "responsable": "..."}}
  ]
}}

Transcripción:
"""

@app.post("/analizar-transcripcion/")
async def analizar_transcripcion(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos .txt")

    contenido = await file.read()
    transcripcion = contenido.decode("utf-8")

    # Prepara el prompt con la transcripción
    prompt = PROMPT_TEMPLATE + transcripcion + '\n"""'

    try:
        # Llama al API de OpenAI para generar los requerimientos técnicos
        response = openai_client.chat.completions.create(
            model="gpt-4",  # Usa el modelo más avanzado disponible
            messages=[
                {"role": "system", "content": "Eres un asistente especializado en análisis de requerimientos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        # Extrae la respuesta generada
        resultado = response.choices[0].message.content

        # Intenta cargar el resultado como JSON
        try:
            resultado_json = json.loads(resultado)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="La respuesta no es un JSON válido")

        # Escribe el resultado en un archivo JSON
        with open("resultado requerimientos.json", "w", encoding="utf-8") as json_file:
            json.dump(resultado_json, json_file, ensure_ascii=False, indent=4)

        return {"message": "Requerimientos escritos en resultado requerimientos.json"}

        return {"requerimientos": resultado}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

# Comando para ejecutar la API
#uvicorn main:app --reload