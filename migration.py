import pymongo

# Conexión a MongoDB
client = pymongo.MongoClient('mongodb+srv://davidpajuelo:SeicN5PUJ5eLTI25@cluster0.qivlt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ia']
collection = db['Recomendaciones']

# Datos de ejemplo para las recomendaciones
datos_recomendaciones =  [
    {'variable': 'usoAnticoagulantes', 'nivel': 1, 'descripcion': 'Consulta a un entrenador personal o profesional de la salud para desarrollar un plan de ejercicios personalizado que sea seguro para ti mientras estás tomando anticoagulantes.'},
    {'variable': 'usoMedicamentosPresion', 'nivel': 1, 'descripcion': 'Practica técnicas de manejo del estrés como la meditación o el yoga para ayudar a controlar tu presión arterial y mejorar tu bienestar general junto con tu medicación.'},
    {'variable': 'cirugiasPrevias', 'nivel': 1, 'descripcion': 'Sigue una dieta rica en nutrientes y alta en proteínas para apoyar la cicatrización y la recuperación después de la cirugía, y evita el consumo de alcohol y tabaco que pueden interferir con tu recuperación.'},
    {'variable': 'actividadesExtenuantes', 'nivel': 1, 'descripcion': 'Considera la posibilidad de trabajar con un fisioterapeuta para desarrollar un programa de rehabilitación específico si realizas actividades extenuantes de forma regular para prevenir lesiones y optimizar tu rendimiento.'},
    {'variable': 'antecedentesCardiovasculares', 'nivel': 1, 'descripcion': 'Mantén un registro regular de tu presión arterial y tus niveles de colesterol y sigue las recomendaciones de tu médico para ajustar tu tratamiento según sea necesario.'},
    {'variable': 'antecedentesCardiacos', 'nivel': 1, 'descripcion': 'Participa en programas de rehabilitación cardíaca supervisados para mejorar tu estado físico y reducir el riesgo de complicaciones cardíacas en personas con antecedentes de problemas cardíacos.'},
    {'variable': 'antecedentesRespiratorios', 'nivel': 1, 'descripcion': 'Evita la exposición prolongada a factores ambientales desencadenantes como la contaminación del aire o el polen si tienes antecedentes respiratorios para prevenir exacerbaciones de tus síntomas.'},
    {'variable': 'antecedentesRenales', 'nivel': 1, 'descripcion': 'Controla tu consumo de líquidos y sigue una dieta baja en proteínas y sodio si tienes antecedentes renales para ayudar a reducir la carga sobre tus riñones y prevenir complicaciones.'},
    {'variable': 'antecedentesDiabeticos', 'nivel': 1, 'descripcion': 'Monitorea regularmente tus niveles de azúcar en sangre y sigue un plan de alimentación saludable y equilibrado bajo la supervisión de un dietista registrado si tienes antecedentes de diabetes para mantener tus niveles de glucosa bajo control.'},
    {'variable': 'antecedentesHipertension', 'nivel': 1, 'descripcion': 'Reduce tu consumo de sodio y sigue una dieta rica en frutas, verduras y productos lácteos bajos en grasa si tienes antecedentes de hipertensión para ayudar a controlar tu presión arterial.'},
    {'variable': 'antecedentesObesidad', 'nivel': 1, 'descripcion': 'Trabaja con un nutricionista para desarrollar un plan de alimentación saludable y sostenible y busca el apoyo de un entrenador personal o un grupo de ejercicio si tienes antecedentes de obesidad para perder peso de manera segura y efectiva.'},
    {'variable': 'antecedentesColesterol', 'nivel': 1, 'descripcion': 'Adopta un estilo de vida activo que incluya ejercicio regular y una dieta rica en fibra, frutas y verduras si tienes antecedentes de colesterol alto para ayudar a reducir tus niveles de colesterol y prevenir enfermedades cardiovasculares.'},
    {'variable': 'fumador', 'nivel': 1, 'descripcion': 'Busca el apoyo de un programa para dejar de fumar o un consejero de salud para ayudarte a dejar de fumar de forma segura y efectiva si eres fumador.'},
    {'variable': 'diabetes', 'nivel': 1, 'descripcion': 'Consulta a un dietista registrado para desarrollar un plan de alimentación personalizado y busca el apoyo de un educador en diabetes para aprender a manejar tu diabetes de manera efectiva.'},
    {'variable': 'actividadFisica', 'nivel': 1, 'descripcion': 'Considera la posibilidad de trabajar con un entrenador personal certificado para desarrollar un programa de ejercicio adaptado a tus necesidades y objetivos específicos.'},
    {'variable': 'alimentacion', 'nivel': 1, 'descripcion': 'Consulta a un dietista registrado para obtener orientación sobre cómo mejorar tu dieta y hacer cambios sostenibles en tu estilo de vida para promover la salud y el bienestar.'},
    {'variable': 'consumoAlcohol', 'nivel': 1, 'descripcion': 'Busca el apoyo de un grupo de apoyo o un terapeuta especializado en el tratamiento del alcoholismo si tienes dificultades para reducir o dejar de consumir alcohol por tu cuenta.'},
    {'variable': 'nivelEstres', 'nivel': 1, 'descripcion': 'Practica técnicas de manejo del estrés como la meditación, la respiración profunda o el yoga para ayudar a reducir los niveles de estrés y mejorar tu bienestar emocional.'}
]

# Insertar datos de ejemplo en la colección
collection.insert_many(datos_recomendaciones)

# Cerrar conexión
client.close()
