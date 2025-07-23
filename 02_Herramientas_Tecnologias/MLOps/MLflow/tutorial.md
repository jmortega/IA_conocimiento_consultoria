# /02_Herramientas_Tecnologias/MLOps/MLflow/tutorial.md
# Tutorial Rápido de MLflow

## Instalación
```bash
pip install mlflow

import mlflow

mlflow.start_run()
mlflow.log_param("learning_rate", 0.01)
mlflow.log_metric("accuracy", 0.85)
mlflow.end_run()