from rest_framework.permissions import BasePermission

from users.constants import Role


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER

    def has_object_permission(self, request, view, obj):
        return obj.manager == request.user


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
