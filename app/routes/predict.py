from flask import request, jsonify
from pymongo import MongoClient
import random
from . import predict_bp
from ..model import modelo

# Conectar a la base de datos MongoDB utilizando la URL de conexión
client = MongoClient('mongodb+srv://davidpajuelo:SeicN5PUJ5eLTI25@cluster0.qivlt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ia']  
collection = db['cuestions']
recomendaciones_collection = db['Recomendaciones']

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    required_params = [
        'actividadFisica',
        'actividadesExtenuantes',
        'alimentacion',
        'antecedentesCardiacos',
        'antecedentesCardiovasculares',
        'antecedentesColesterol',
        'antecedentesDiabeticos',
        'antecedentesHipertension',
        'antecedentesObesidad',
        'antecedentesRenales',
        'antecedentesRespiratorios',
        'cirugiasPrevias',
        'consumoAlcohol',
        'diabetes',
        'edad_cardiovascular',
        'fumador',
        'nivelEstres',
        'sex',
        'usoAnticoagulantes',
        'usoMedicamentosPresion',
        
    ]
    print(data)
    for param in required_params:
        if param not in data:
            return jsonify({'error': f'Missing parameter: {param}'}), 400

    # Realizar la predicción utilizando el modelo y los datos recibidos
    datos_de_prueba = [[data[param] for param in required_params]]
    predicciones = modelo.predict(datos_de_prueba)

    # Guardar los datos en MongoDB
    data['_id'] = str(db.collection.count_documents({}) + 1)  
    db.collection.insert_one(data)

    # Obtener recomendaciones asociadas a las respuestas
    recomendaciones = {}
    for param, value in data.items():
        recomendacion = recomendaciones_collection.find_one({'variable': param, 'nivel': value})
        if recomendacion:
            recomendaciones[param] = recomendacion['descripcion']

    # Convertir las recomendaciones a una lista de tuplas
    recomendaciones_list = list(recomendaciones.items())

    # Limitar la cantidad de recomendaciones a entre 2 y 3
    cantidad_recomendaciones = random.randint(2, 3)
    recomendaciones_aleatorias = dict(random.sample(recomendaciones_list, cantidad_recomendaciones))

    return jsonify({'success': True, 'predict': int(predicciones[0]), 'recomendaciones': recomendaciones_aleatorias})
