#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 28.12.14.
"""

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', 'updated')
    list_filter = ('created',)
    search_fields = ('author__username',)
    ordering = ('created',)


admin.site.register(Post, PostAdmin)

