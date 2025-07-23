# /02_Herramientas_Tecnologias/LLMs_PLN/Gemini/guia_implementacion.md
# Guía de Implementación: Gemini

## Configuración Vertex AI
1. Activar Vertex AI en Google Cloud
2. Crear servicio account con permisos
3. Habilitar facturación

## Ejemplo de Uso
```python
import vertexai
from vertexai.preview.generative_models import GenerativeModel

vertexai.init(project="tu-proyecto", location="us-central1")
model = GenerativeModel("gemini-pro")
response = model.generate_content("Resume este texto...")
print(response.text)