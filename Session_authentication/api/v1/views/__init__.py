#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

# Initialisation de Blueprint avant les imports des autres modules
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.session_auth import *
from api.v1.views.users import *
from api.v1.views.index import *

# Assurez-vous que la classe User est correctement définie et accessible
User.load_from_file()
