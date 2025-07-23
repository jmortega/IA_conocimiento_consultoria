# /04_Casos_Uso/Plantillas_Soluciones/chatbot_atencion_cliente/flujo_conversacion.md
# Flujo de Conversación: Chatbot Inteligente

## Diseño de Diálogos
```mermaid
stateDiagram-v2
    [*] --> Saludo
    Saludo --> Intencion: Detecta objetivo usuario
    Intencion --> ConsultaBD: 60% casos
    Intencion --> AgenteHumano: 15% complejidad
    Intencion --> Proceso: 25% transacciones