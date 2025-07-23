# /02_Herramientas_Tecnologias/LLMs_PLN/OpenAI/guia_implementacion.md
# Guía de Implementación: OpenAI API

## Configuración Inicial
1. Registro en platform.openai.com
2. Generación de API key
3. Instalación SDK: `pip install openai`

## Uso Básico
```python
from openai import OpenAI
client = OpenAI(api_key="tu-api-key")

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[{"role": "user", "content": "Explica la IA generativa"}]
)
print(response.choices[0].message.content)