# /02_Herramientas_Tecnologias/LLMs_PLN/HuggingFace/guia_transformers.md
# Guía Transformers de HuggingFace

## Instalación
```bash
pip install transformers datasets torch

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("Me encanta este repositorio!")
print(result)


from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)
trainer.train()
