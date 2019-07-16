# -*- coding: utf-8 -*-
from flask import Blueprint

from flask_rest_jsonapi import Api

from .users import UserList, UserDetail, MeResource
from .authentication import UserRegister
from .admin.permissions import PermissionDetail, PermissionList
from .admin.profiles import ProfileDetail, ProfileList


json_api = Blueprint('api_prefix', __name__, url_prefix='/api/v1')
api = Api(blueprint=json_api)
api.route(UserList, 'user_list', '/users')
api.route(MeResource, 'me', '/me')
api.route(UserDetail, 'user_detail', '/users/<int:id>')
api.route(UserRegister, 'user_register_list', '/singup')
api.route(PermissionList, 'permission_list', '/permissions')
api.route(PermissionDetail, 'permission_detail', '/permissions/<int:id>')
api.route(ProfileList, 'profile_list', '/profiles')
api.route(ProfileDetail, 'profile_detail', '/profiles/<int:id>')
