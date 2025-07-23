# /05_Datos_Gobernanza/Versionado/data_lineage.md
# Gestión de Lineage de Datos en Proyectos IA

## Componentes Clave
1. **Orígenes**: 
   - APIs, bases de datos, archivos crudos
   - Metadatos de procedencia

2. **Transformaciones**:
   - Scripts de ETL/limpieza versionados
   - Parámetros de procesamiento

3. **Consumidores**:
   - Modelos que usan cada dataset
   - Reportes/dashboards generados

## Herramientas Recomendadas
- **OpenLineage**: Estándar abierto
- **Apache Atlas**: Para entornos enterprise
- **Custom Metadata**: Con ML Metadata (MLMD)

## Visualización
```mermaid
graph LR
    A[Fuente CRM] --> B[(Lago de Datos)]
    B --> C{Transformación}
    C --> D[Dataset Entrenamiento]
    C --> E[Dataset Validación]
    D --> F[Modelo XGBoost]
    E --> F