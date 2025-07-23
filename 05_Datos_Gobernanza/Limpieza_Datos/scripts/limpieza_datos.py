# /05_Datos_Gobernanza/Limpieza_Datos/scripts/limpieza_datos.py
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def clean_dataset(df):
    """Pipeline básico de limpieza para datos tabulares"""
    # 1. Eliminar duplicados
    df = df.drop_duplicates()
    
    # 2. Manejo de valores faltantes
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(exclude=np.number).columns
    
    if len(num_cols) > 0:
        num_imputer = SimpleImputer(strategy='median')
        df[num_cols] = num_imputer.fit_transform(df[num_cols])
    
    if len(cat_cols) > 0:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])
    
    # 3. Normalización básica
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    return df

# Uso recomendado:
# df = pd.read_csv('datos_sin_limpiar.csv')
# df_clean = clean_dataset(df)