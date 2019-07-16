# -*- coding: utf-8 -*-
from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi.exceptions import InvalidField

from ...models import db
from ...models.users import Permission
from ...schemas.admin.permissions import PermissionSchema
from ...core.mixins import ResourceDetailMixin


def before_create_object(self, data, view_kwargs):
    permission = Permission.query.filter_by(name=data['name']).first()
    name = data['name'].lower()
    tables_names = db.metadata.tables.keys()
    if permission:
        raise InvalidField(
            detail='Permission with this name already exists',
            source={'pointer': '/data/attributes/name'},
            title="Validation error"
        )

    data["is_crud"] = (name in tables_names)
    return data


class PermissionList(ResourceList):

    schema = PermissionSchema
    data_layer = {
        'session': db.session,
        'model': Permission,
        'methods': {'before_create_object': before_create_object}
    }


class PermissionDetail(ResourceDetail):

    schema = PermissionSchema
    data_layer = {
        'session': db.session,
        'model': Permission,
        'methods': {'before_get_object': ResourceDetailMixin.before_get_object}
    }
