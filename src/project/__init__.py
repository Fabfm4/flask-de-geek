# -*- coding: utf-8 -*-
from flask import Flask

from .models import bcrypt, db
from .api import api
from .core.authentication import jwt


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('APP_CONFIG_FILE')
    db.init_app(app)
    bcrypt.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    return app


app = create_app()
