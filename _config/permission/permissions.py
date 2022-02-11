from docutils.parsers.rst.directives.misc import Role
from rest_framework.permissions import BasePermission
from user.models import *


class IsUser(BasePermission):
    """
    Allows access only to "onepay" users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_user == True and request.user.is_active


class IsAdmin(BasePermission):
    """
    Allows access only to "admin" users.
    """
    message = 'Only admin have permission to perform this action.'

    def has_permission(self, request, view):
        return request.user and request.user.is_admin == True and request.user.is_active


class IsSupAdmin(BasePermission):
    """
    Allows access only to "super admin" users.
    """
    message = 'Only super admin have permission to perform this action.'

    def has_permission(self, request, view):
        return request.user and request.user.is_super_admin == True and request.user.is_active
class IsMerchant(BasePermission):
    """
    Allows access only to "super admin" users.
    """
    message = 'Only merchant have permission to perform this action.'

    def has_permission(self, request, view):
        return request.user and request.user.is_merchant == True and request.user.is_active

class IsDigitaluser(BasePermission):
    """
    Allows access only to "super admin" users.
    """
    message = 'Only digital user have permission to perform this action.'

    def has_permission(self, request, view):
        return request.user and request.user.is_digitaluser == True and request.user.is_active