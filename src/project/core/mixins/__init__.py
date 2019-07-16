# -*- coding: utf-8 -*-
from flask_rest_jsonapi.exceptions import ObjectNotFound
from flask_rest_jsonapi import ResourceDetail


class ResourceDetailMixin(object):

    def before_get_object(self, values_kwargs):
        pk = values_kwargs.get('id')
        object_model = self.model.query.filter_by(id=pk).first()
        if not object_model:
            raise ObjectNotFound('detail')

        return object_model
