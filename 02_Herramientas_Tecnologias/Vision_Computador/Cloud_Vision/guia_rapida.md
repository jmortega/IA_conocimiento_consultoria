# /02_Herramientas_Tecnologias/Vision_Computador/Cloud_Vision/guia_rapida.md
# Guía Rápida: Google Cloud Vision

## Servicios Principales
- Etiquetado de imágenes
- Detección de objetos/caras
- OCR (texto en imágenes)
- Safe Search (contenido explícito)

## Ejemplo API
```python
from google.cloud import vision

client = vision.ImageAnnotatorClient()
image = vision.Image(content=image_bytes)
response = client.label_detection(image=image)

for label in response.label_annotations:
    print(label.description, label.score)