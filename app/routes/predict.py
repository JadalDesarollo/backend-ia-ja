from flask import request, jsonify
from . import predict_bp
from ..model import modelo
@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    required_params = ['edad_cardiovascular', 'targa', 'hepatitisB', 'hepatitisC', 'VIH', 'sida', 'tuberculosis', 'insRespiratoria', 'alcoholismo', 'anemia', 'desnutricion', 'cancer', 'diarrea', 'diabetes','sepsis', 'neumonia', 'covid','test1','test2','test3']
    for param in required_params:
        if param not in data:
            return jsonify({'error': f'Missing parameter: {param}'}), 400

    # Realizar la predicción utilizando el modelo y los datos recibidos
    datos_de_prueba = [[data[param] for param in required_params]]
    predicciones = modelo.predict(datos_de_prueba)

    return jsonify({'success': True, 'predict': int(predicciones[0])})
