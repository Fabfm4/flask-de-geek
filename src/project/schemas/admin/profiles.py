# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class ProfileSchema(Schema):

    class Meta:
        type_ = 'profile'
        self_view = 'api_prefix.profile_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.profile_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(required=True)
