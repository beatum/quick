#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 28.12.14.
"""

from django.contrib import admin
from quick.posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('author__username',)
    ordering = ('created_at',)


admin.site.register(Post, PostAdmin)

