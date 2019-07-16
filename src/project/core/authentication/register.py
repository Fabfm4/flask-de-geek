# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from ...models.users import Profile, User
from flask_rest_jsonapi.exceptions import InvalidField


def before_create_object(self, data, view_kwargs):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        raise InvalidField(
            detail='User with this email already exists',
            source={'pointer': '/data/attributes/email'},
            title="Validation error"
        )
    profile = Profile.query.filter_by(name="app").first()
    data['profile_id'] = profile.id


class UserRegisterSchema(Schema):

    class Meta:
        type_ = 'register'
        self_view = 'api_prefix.user_register_list'

    id = fields.Integer(as_string=True, dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=False, load_only=True)
    profile_id = fields.Integer(as_string=True, dump_only=True, load_only=True)
