# /06_Capacitacion_Desarrollo/Cursos_Internos/introduccion_IA/ejercicios/ejercicio1.py
"""
Ejercicio 1: Primer Modelo de ML
Objetivo: Entrenar un modelo de regresión lineal con scikit-learn
"""

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar datos
data = load_diabetes()
X, y = data.data, data.target

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluar
score = model.score(X_test, y_test)
print(f"R² Score: {score:.2f}")

# Tarea adicional:
# 1. Graficar predicciones vs reales
# 2. Probar con otro algoritmo (ej. RandomForest)