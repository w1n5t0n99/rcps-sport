from flask import Blueprint

main = Blueprint('main', __name__)
# imported after main instantiated to avoid circular dependency problems
from . import views, errors


