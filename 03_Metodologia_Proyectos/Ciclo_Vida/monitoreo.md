# /03_Metodologia_Proyectos/Ciclo_Vida/monitoreo.md
# Monitoreo de Modelos en Producción

## Métricas Clave a Seguir
- **Desempeño**: Accuracy, latency, throughput
- **Data Drift**: Cambios en distribución de entrada
- **Concept Drift**: Cambios en relaciones entrada-salida
- **Infraestructura**: Uso CPU/GPU, memoria

## Herramientas Recomendadas
- Evidently AI
- Amazon SageMaker Model Monitor
- Prometheus + Grafana
- Custom dashboards

## Protocolo de Alertas
1. Detección anomalía
2. Clasificación severidad
3. Notificación equipo responsable
4. Acción correctiva documentada