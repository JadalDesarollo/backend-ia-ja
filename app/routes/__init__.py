from flask import Blueprint

predict_bp = Blueprint('predict', __name__)
auth_bp = Blueprint('auth', __name__)

from . import predict
from . import auth
