from flask import Blueprint


authentification = Blueprint('authentification'.__name__)

from . import routes