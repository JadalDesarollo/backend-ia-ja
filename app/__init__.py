from flask import Flask
from .routes.predict import predict_bp
from .routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Registrar los blueprints
    app.register_blueprint(predict_bp)
    app.register_blueprint(auth_bp)

    return app
