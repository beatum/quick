#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""
# from rest_framework import permissions
#
#
# class SafeMethodsOnlyPermission(permissions.BasePermission):
#     """
#     Only can access non-destructive methods (like GET and HEAD)
#     """
#     def has_permission(self, request, view):
#         return self.has_object_permission(request, view)
#
#     def has_object_permission(self, request, view, obj=None):
#         return request.method in permissions.SAFE_METHODS
#
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Write permissions are only allowed to the owner of the snippet
#         return obj.user == request.user
