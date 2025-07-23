# /04_Casos_Uso/por_Industria/Salud/procesamiento_historias/nlp_clinico.md
# NLP para Procesamiento de Historias Clínicas

## Funcionalidades Clave
1. **NER Médico**: Detección de:
   - Enfermedades (CIE-10)
   - Medicamentos (Vademécum)
   - Procedimientos
2. **Resumen Automático**: Para rondas médicas
3. **Clasificación**: Priorización casos

## Stack Tecnológico
- **Modelos**: BioClinicalBERT + CRF
- **Preprocesamiento**: Apache cTAKES
- **Postprocesamiento**: Reglas SNOMED-CT

## Resultados Validación
| Tarea | F1-score |
|-------|----------|
| NER | 0.91 |
| Resumen | ROUGE-0.72 |
| Clasificación | 0.89 |