# /05_Datos_Gobernanza/Limpieza_Datos/tecnicas.md
# Técnicas Avanzadas de Limpieza de Datos

## Para Datos Estructurados
- **Outliers**:
  - Detección: Isolation Forest, DBSCAN
  - Tratamiento: Winsorization, imputación robusta

- **Inconsistencias**:
  - Validación con reglas de negocio (Great Expectations)
  - Corrección automática con fuzzy matching

## Para Texto
- Normalización Unicode
- Corrección ortográfica (SymSpell, HunSpell)
- Detección idioma (fastText)

## Para Imágenes
- Reducción de ruido (OpenCV)
- Normalización de histograma
- Eliminación de artefactos (DL-based)