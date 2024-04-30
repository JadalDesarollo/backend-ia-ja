
# Proyecto de Predicción de Salud

Este proyecto proporciona una API para predecir el estado de salud de un paciente utilizando un modelo de aprendizaje automático.

## Configuración del Entorno y Prueba de la API

### Crear un Entorno Virtual

1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio de tu proyecto.
3. Ejecuta el siguiente comando para crear un nuevo entorno virtual llamado `venv`:

```bash
python3 -m venv venv  # Linux/macOS
# o
python -m venv venv  # Windows
```

### Activar el Entorno Virtual

4. Activa el entorno virtual con el siguiente comando:

```bash
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate  # Windows
```

### Instalación de Dependencias

5. Instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecutar la API

6. Inicia el servidor Flask para ejecutar la API. Se tiene un archivo `run.py` que contiene la definición de tu aplicación Flask. Ejecuta el siguiente comando para iniciar el servidor:

```bash
python run.py
```

### Probar la API

7. Una vez que el servidor esté en funcionamiento, puedes probar la API enviando una solicitud POST con el siguiente JSON a la ruta `/predict`:

```json
{
    "edad_cardiovascular": 30,
    "sex": 1,
    "usoAnticoagulantes": 1,
    "usoMedicamentosPresion": 0,
    "cirugiasPrevias": 0,
    "actividadesExtenuantes": 1,
    "antecedentesCardiovasculares": 1,
    "antecedentesCardiacos": 0,
    "antecedentesRespiratorios": 1,
    "antecedentesRenales": 0,
    "antecedentesDiabeticos": 0,
    "antecedentesHipertension": 0,
    "antecedentesObesidad": 0,
    "antecedentesColesterol": 0,
    "fumador": 0,
    "diabetes": 0,
    "actividadFisica": 0,
    "alimentacion": 1,
    "consumoAlcohol": 1,
    "nivelEstres": 1
}
```

8. Recibirás una respuesta JSON con los resultados de la predicción y las recomendaciones.

### Desactivar el Entorno Virtual

9. Cuando hayas terminado de trabajar con la aplicación, puedes desactivar el entorno virtual con el siguiente comando:

```bash
deactivate
```

Con esto, has creado un entorno virtual, instalado las dependencias necesarias, ejecutado la API y probado su funcionalidad utilizando la solicitud JSON proporcionada.
