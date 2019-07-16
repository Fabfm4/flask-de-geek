# -*- coding: utf-8 -*-
from flask_jwt import JWT, _jwt_required, CONFIG_DEFAULTS, current_identity, JWTError
from flask import request
from functools import wraps
from ...models.users import Permission, User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if user.is_active and user.verify_password(password):
            return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id)


def check_user_has_permission(user, permission):
    permission = Permission.query.filter_by(name=permission).first()
    has_permission = True
    if permission:
        has_permission = False
        method = request.environ['REQUEST_METHOD']
        matrix_permissions = user.profile.matrix_permissions.filter_by(
            permission_id=permission.id
        ).first()
        if matrix_permissions:
            has_permission = True
            if permission.is_crud:
                has_permission = False
                if method == 'GET' and matrix_permissions.can_view:
                    has_permission = True

                if method == 'POST' and matrix_permissions.can_create:
                    has_permission = True

                if method == 'DELETE' and matrix_permissions.can_delete:
                    has_permission = True

                if method == 'PUT' and matrix_permissions.can_edit:
                    has_permission = True

                if method == 'PATCH' and matrix_permissions.can_edit:
                    has_permission = True

    return has_permission


def jwt_required_custom(realm=None, permission=None):
    """View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """
    def wrapper(fn, *args, **kwargs):
        @wraps(fn)
        def decorator(*args, **kwargs):
            _jwt_required(realm or CONFIG_DEFAULTS['JWT_DEFAULT_REALM'])
            if not check_user_has_permission(
                current_identity.first(), permission
            ):
                raise JWTError(
                    'Access denied', 'access denied', status_code=403
                )
            return fn(*args, **kwargs)
        return decorator
    return wrapper


jwt = JWT(None, authenticate, identity)
