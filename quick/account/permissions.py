#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 27.12.14.
"""
from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    """
    Set base account permission
    """
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False