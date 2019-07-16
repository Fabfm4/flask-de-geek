# -*- coding: utf-8 -*-
from flask_rest_jsonapi import ResourceList

from ...core.authentication.register import (
    before_create_object, UserRegisterSchema
)
from ...models import db
from ...models.users import User


class UserRegister(ResourceList):

    methods = ['POST']
    schema = UserRegisterSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {'before_create_object': before_create_object}
    }
