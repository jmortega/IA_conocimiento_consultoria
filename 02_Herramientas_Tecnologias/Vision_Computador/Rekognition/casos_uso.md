# /02_Herramientas_Tecnologias/Vision_Computador/Rekognition/casos_uso.md
# Casos de Uso: AWS Rekognition

## Aplicaciones Comunes
1. **Moderación de contenido**: Detección de contenido inapropiado
2. **Seguridad**: Reconocimiento facial para acceso
3. **Retail**: Análisis de estanterías en tiendas
4. **Medios**: Búsqueda en bibliotecas de vídeo
5. **Accesibilidad**: Descripción automática de imágenes

## Ejemplo Implementación
```python
import boto3

client = boto3.client('rekognition')
response = client.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=10
)
print(response['Labels'])