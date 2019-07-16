# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserSchema(Schema):

    class Meta:
        type_ = 'user'
        self_view = 'api_prefix.user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.user_list'

    id = fields.Integer(as_string=True, dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=False, dump_only=True, load_only=True)
    is_active = fields.Boolean(required=False, default=True)
    created = fields.DateTime(required=False)
    updated = fields.DateTime(required=False)
