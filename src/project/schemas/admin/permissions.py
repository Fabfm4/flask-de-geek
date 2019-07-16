# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class PermissionSchema(Schema):

    class Meta:
        type_ = 'permission'
        self_view = 'api_prefix.permission_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.permission_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(default='')
    is_crud = fields.Boolean(default=False)
    created = fields.DateTime(required=False, dump_only=True)
    updated = fields.DateTime(required=False, dump_only=True)
