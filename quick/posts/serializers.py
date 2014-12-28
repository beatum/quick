from rest_framework import serializers
#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 28.12.14.
"""


from quick.authentication.serializers import AccountSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']
