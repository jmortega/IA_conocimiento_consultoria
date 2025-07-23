# /04_Casos_Uso/por_Industria/Finanzas/deteccion_fraude/lecciones.md
# Lecciones Aprendidas: Detección de Fraude

## Técnicas Efectivas
- Balanceo de datos con SMOTE
- Ensemble de modelos (Isolation Forest + Autoencoder)
- Feature engineering temporal (patrones horarios)

## Desafíos Superados
- **Falsos positivos**: Mejorado con reglas de negocio
- **Latencia**: Optimizado con ONNX runtime
- **Actualización modelo**: Pipeline CI/CD semanal

## Recomendaciones
1. Priorizar recall sobre precisión inicialmente
2. Incluir feedback de analistas humanos
3. Monitorear drift de comportamiento