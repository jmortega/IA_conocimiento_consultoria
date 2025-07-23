# /04_Casos_Uso/por_Industria/Retail/analisis_sentimiento/metricas.md
# Métricas: Análisis de Sentimiento

## Rendimiento Técnico
- **Accuracy**: 89.4%
- **F1-score (negativo)**: 0.83
- **Latencia p95**: 127ms

## Impacto Operacional
- **Tiempo respuesta quejas**: De 5.2d a 1.4d
- **Detección temprana crisis**: 3 eventos evitados/mes
- **Optimización inventario**: Correlación 0.72 con ventas

## Benchmarking
| Modelo | Costo | Precisión |
|--------|-------|-----------|
| BERT Base | $1.2/hora | 87.2% |
| DistilBERT | $0.7/hora | 85.1% |
| Nuestro Modelo | $0.9/hora | 89.4% |