# -*- coding: utf-8 -*-
from datetime import timedelta


SQLALCHEMY_DATABASE_URI = 'postgresql://docker:docker@postgresql/whereareyou'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '\x93<\x83\x83\xfcV\x19\x96\x10K\xd4\xe4<z(/`\x1e\x9eo\x12Z\x1c\xbd'
JWT_AUTH_USERNAME_KEY = 'email'
JWT_AUTH_URL_RULE = '/api/v1/signin'
JWT_LEEWAY = timedelta(seconds=10)
JWT_EXPIRATION_DELTA = timedelta(seconds=604800)
