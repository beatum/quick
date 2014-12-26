#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# API
urlpatterns += (
    url(r'^', include('quick.account.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)