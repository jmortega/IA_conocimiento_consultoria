# /04_Casos_Uso/por_Industria/Finanzas/deteccion_fraude/caso_estudio.md
# Caso de Estudio: Detección de Fraude en Transacciones Financieras

## Contexto del Cliente
- **Sector**: Banca digital
- **Volumen**: 2M transacciones/día
- **Problema**: 0.7% tasa de fraude no detectada

## Solución Implementada
```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    n_estimators=150,
    contamination=0.007,
    random_state=42
)
model.fit(train_data)

# Features clave:
# - Hora transacción
# - Dispositivo origen
# - Historial usuario
# - Monto/ubicación