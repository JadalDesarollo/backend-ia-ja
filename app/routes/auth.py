from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from . import auth_bp
import jwt
from jwt import encode
from pymongo import MongoClient
from flask import Blueprint
import datetime 
from functools import wraps
from bson import ObjectId
client = MongoClient('mongodb+srv://davidpajuelo:SeicN5PUJ5eLTI25@cluster0.qivlt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ia']
usuarios_collection = db['usuarios']
SECRET_KEY = 'asasasas232edqsd232'

# Función para verificar la autenticación del usuario con JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({'error': 'Token is missing'}), 401

        parts = auth_header.split()

        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({'error': 'Invalid token format'}), 401

        token = parts[1]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            
            current_user = usuarios_collection.find_one({'_id':  ObjectId(data['user_id'])})
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        if not current_user:
            return jsonify({'error': 'User not found'}), 404

        return f(current_user, *args, **kwargs)

    return decorated

@auth_bp.route('/register', methods=['POST'])
def registro():
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Verificar si los datos están completos
    if not username or not email or not password:
        return jsonify({'success': False,'error': 'Todos los campos son obligatorios'}), 400

    # Verificar si el correo electrónico ya está registrado
    if usuarios_collection.find_one({'email': email}):
        return jsonify({'success': False,'error': 'El correo electrónico ya está registrado'}), 400

    # Encriptar la contraseña
    hashed_password = generate_password_hash(password)

    # Crear el documento del usuario
    user_data = {
        'username': username,
        'email': email,
        'password': hashed_password
    }

    # Guardar el usuario en la base de datos
    usuarios_collection.insert_one(user_data)

    return jsonify({'success': True, 'message': 'Usuario registrado exitosamente'}), 200
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not data or not email or not password:
        return jsonify({'success': False, 'error': 'Formulario incompleto'}), 401

    user = usuarios_collection.find_one({'email': email})

    if not user:
        return jsonify({'success': False,'error': 'Usuario o contraseña incorrectas'}), 401

    if check_password_hash(user['password'], password):
        token = encode({'user_id': str(user['_id']), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm="HS256")
        return jsonify({'success': True,'user': str(user['username']),'token': token}), 200

    return jsonify({'success': False,'error': 'Usuario o contraseña incorrectas'}), 401

@auth_bp.route('/refresh_token', methods=['POST'])
@token_required
def refresh_token(current_user):
    token =encode({'user_id': str(current_user['_id']), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm="HS256")
    return jsonify({'success': True,'user':str(current_user['username']),'token': token}), 200