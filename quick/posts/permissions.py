#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 28.12.14.
"""


from rest_framework import permissions


class IsAuthorOfPost(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user:
            return post.author == request.user
        return False
