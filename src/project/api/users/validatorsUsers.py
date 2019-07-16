# -*- coding: utf-8 -*-
from email_validator import validate_email, EmailNotValidError
from flask_rest_jsonapi.exceptions import InvalidField


class UserCreateValidate(object):

    def before_post_mixin(self, model, *args, **kwargs):

        if model.query.filter_by(email=kwargs["data"]["email"]).first():
            raise InvalidField(
                'Email already exists',
                source={'pointer': '/data/attributes/email'},
                title='Invalid fields querystring pointer.'
            )
