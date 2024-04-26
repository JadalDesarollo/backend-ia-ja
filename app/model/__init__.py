from joblib import load
import os
# Obtener la ruta del directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))
modelo_path = os.path.join(dir_path, 'modelo_entrenado.joblib')
modelo = load(modelo_path)
