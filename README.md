
# Proyecto de Predicción de Salud

Este proyecto proporciona una API para predecir el estado de salud de un paciente utilizando un modelo de aprendizaje automático.

## Instalación

1. **Clona el Repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/proyecto-prediccion-salud.git
   ```
2. **Accede al Directorio del Proyecto**:

   ```bash
   cd proyecto-prediccion-salud
   ```
3. **Instala las Dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. **Crea el Entorno Virtual** (opcional):

   ```bash
   python -m venv venv
   ```
2. **Ejecuta la Aplicación**:

   ```bash
   python run.py
   ```

## Prueba del Endpoint de Predicción

Puedes probar el endpoint de predicción utilizando cualquier cliente HTTP como cURL o Postman. Aquí tienes un ejemplo utilizando cURL:

```bash
curl -X POST \
  http://127.0.0.1:5000/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "edad_cardiovascular": 30,
    "Targa": 1,
    "HepatitisB": 0,
    "HepatitisC": 0,
    "VIH": 1,
    "Sida": 1,
    "Tuberculosis": 0,
    "InsRespiratoria": 1,
    "Alcoholismo": 0,
    "Anemia": 0,
    "Desnutricion": 0,
    "Cancer": 0,
    "Diarrea": 0,
    "Diabetes": 0,
    "Sepsis": 0,
    "Neumonia": 0,
    "Covid": 0
}'
```
