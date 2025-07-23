# /03_Metodologia_Proyectos/Ciclo_Vida/despliegue.md
# Fase de Despliegue en Producción

## Estrategias
- **Canary Release**: Despliegue progresivo
- **Shadow Mode**: Ejecución paralela sin impacto
- **Blue-Green**: Intercambio instantáneo

## Componentes Clave
- API REST/gRPC para inferencia
- Contenerización (Docker)
- Orquestación (Kubernetes)
- Auto-scaling configurado

## Checklist Pre-lanzamiento
- [ ] Pruebas de carga completadas
- [ ] Monitoreo implementado
- [ ] Plan rollback definido
- [ ] Documentación actualizada