from flask import Blueprint,app


authentification = Blueprint('authentification'.__name__)

from . import routes