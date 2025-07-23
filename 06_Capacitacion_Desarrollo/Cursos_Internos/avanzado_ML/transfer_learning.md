# /06_Capacitacion_Desarrollo/Cursos_Internos/avanzado_ML/transfer_learning.md

# Transfer Learning para Visión por Computadora

## Objetivo
Fine-tuning de ResNet50 para clasificación de imágenes médicas

```python
import tensorflow as tf
from tensorflow.keras.applications import ResNet50

# Cargar modelo base
base_model = ResNet50(weights='imagenet', include_top=False)

# Congelar capas
for layer in base_model.layers:
    layer.trainable = False

# Añadir nuevas capas
x = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
predictions = tf.keras.layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs=base_model.input, outputs=predictions)

# Compilar
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])