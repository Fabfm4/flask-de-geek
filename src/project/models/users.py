# -*- coding: utf-8 -*-
from ..models import db, UserMixin, PermissionMixin, CatalogueMixin, RoleMixin, TimeStampedMixin


class Permission(PermissionMixin, db.Model):

    roles = db.relationship(
        'RolePermission',
        backref='permission',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )


class Role(RoleMixin, db.Model):
    permissions = db.relationship(
        'RolePermission',
        backref='role',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )


class RolePermission(TimeStampedMixin, db.Model):
    __tablename__ = 'role_permission'

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))
    __table_args__ = (
        db.UniqueConstraint(
            'role_id',
            'permission_id',
            name='role_permission'),
    )


class User(UserMixin, db.Model):

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


