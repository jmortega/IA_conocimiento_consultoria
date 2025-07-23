# /05_Datos_Gobernanza/Privacidad/anonimizacion.md
# Técnicas de Anonimización de Datos

## Métodos Comprobados
1. **Generalización**:
   - Rangos de edad en lugar de exacta
   - Regiones geográficas en lugar de direcciones

2. **Supresión**:
   - Eliminación de identificadores directos
   - Masking de datos sensibles (ej. tarjetas crédito)

3. **Perturbación**:
   - Adición de ruido controlado
   - Swapping de valores entre registros

4. **Diferenciación Privada**:
   - k-anonymity (k > 5 recomendado)
   - l-diversity
   - t-closeness

## Herramientas Recomendadas
- ARX (para datos tabulares)
- Presidio (Microsoft)
- Faker (para datos sintéticos)