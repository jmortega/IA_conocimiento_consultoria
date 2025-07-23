# /04_Casos_Uso/por_Industria/Finanzas/scoring_credito/enfoque.md
# Enfoque: Sistema de Scoring Crediticio con IA

## Arquitectura Técnica
- **Fuentes datos**:
  - Historial crediticio
  - Transacciones bancarias
  - Datos alternativos (telco, utilities)

- **Model Stack**:
  1. XGBoost (predicción principal)
  2. Red neuronal (segunda opinión)
  3. Sistema de reglas (compliance)

## Innovaciones Clave
- Explainability por diseño (SHAP values)
- Actualización dinámica con nuevos pagos
- Segmentación por perfiles demográficos