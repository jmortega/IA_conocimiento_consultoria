# /05_Datos_Gobernanza/Etiquetado_Datos/guia_etiquetado.md
# Guía Completa de Etiquetado de Datos

## Protocolos por Tipo de Dato
1. **Imágenes**:
   - Bounding boxes (COCO format)
   - Segmentación semántica (VOC format)
   - Atributos múltiples (CVAT)

2. **Texto**:
   - NER (BIO tagging)
   - Clasificación de intención
   - Anotación de relaciones (BRAT)

3. **Audio**:
   - Transcripciones verbatim
   - Etiquetado emocional
   - Identificación de speakers

## Control de Calidad
- Revisión cruzada entre anotadores
- Métricas de concordancia (Cohen's Kappa > 0.8)
- Auditorías aleatorias (5-10% del dataset)