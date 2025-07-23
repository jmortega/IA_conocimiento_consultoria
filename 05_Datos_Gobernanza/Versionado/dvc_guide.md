# /05_Datos_Gobernanza/Versionado/dvc_guide.md
# Guía Práctica de DVC para Versionado de Datos

## Flujo de Trabajo Básico
```bash
# Inicialización
dvc init
dvc remote add -d myremote /path/to/remote

# Añadir dataset
dvc add data/raw_dataset
git add data/raw_dataset.dvc .gitignore
git commit -m "Add raw dataset version 1"

# Actualización posterior
dvc add data/raw_dataset --force
git commit -am "Update to dataset version 2"
dvc push