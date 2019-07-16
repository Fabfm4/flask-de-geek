# -*- coding: utf-8 -*-
from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi.exceptions import InvalidField

from ...models import db
from ...models.users import Profile
from ...schemas.admin.profiles import ProfileSchema
from ...core.mixins import ResourceDetailMixin


def before_create_object(self, data, view_kwargs):
    profile = Profile.query.filter_by(name=data['name']).first()
    if profile:
        raise InvalidField(
            detail='Profile with this name already exists',
            source={'pointer': '/data/attributes/name'},
            title="Validation error"
        )


def after_create_object(self, obj, data, view_kwargs):
    print(obj)


class ProfileList(ResourceList):

    schema = ProfileSchema
    data_layer = {
        'session': db.session,
        'model': Profile,
        'methods': {
            'before_create_object': before_create_object,
            'after_create_object': after_create_object
        }
    }


class ProfileDetail(ResourceDetail):

    schema = ProfileSchema
    data_layer = {
        'session': db.session,
        'model': Profile,
        'methods': {'before_get_object': ResourceDetailMixin.before_get_object}
    }
