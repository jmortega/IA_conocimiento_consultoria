# /04_Casos_Uso/por_Industria/Retail/sistemas_recomendacion/arquitectura.md
# Arquitectura: Sistema de Recomendación para E-commerce

## Componentes Principales
```mermaid
graph TD
    A[Eventos Usuario] --> B(Streaming Pipeline)
    B --> C[Feature Store]
    D[Catálogo Productos] --> E[Embedding Model]
    C --> F[Ranking Model]
    E --> F
    F --> G[API Recomendaciones]