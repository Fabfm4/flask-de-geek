# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from ..models import bcrypt, db


class TimeStampedMixin(object):

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class CatalogueMixin(TimeStampedMixin):

    name = db.Column(db.String(600), nullable=True)
    is_active = db.Column(db.Boolean())


class UserMixin(TimeStampedMixin):

    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.Binary(120), nullable=True)
    is_active = db.Column(db.Boolean(), default=True)
    login_with_password = True
    __tablename__ = 'users'

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    @hybrid_method
    def verify_password(self, password):
        if self._password:
            return bcrypt.check_password_hash(self._password, password)


class PermissionMixin(CatalogueMixin):
    key = db.Column(db.String(50), unique=True)
    __tablename__ = 'permissions'


class RoleMixin(CatalogueMixin):
    description = db.Column(db.String(120), nullable=True)
    never_delete = db.Column(db.Boolean, default=False, nullable=True)
    __tablename__ = 'roles'
