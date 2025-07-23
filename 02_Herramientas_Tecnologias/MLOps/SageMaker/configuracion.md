# /02_Herramientas_Tecnologias/MLOps/SageMaker/configuracion.md
# Configuración Básica de SageMaker

## Pasos Iniciales
1. Crear rol IAM con permisos SageMaker
2. Configurar VPC y seguridad
3. Crear bucket S3 para datos

## Notebook Instance
```python
import sagemaker
sess = sagemaker.Session()
role = sagemaker.get_execution_role()