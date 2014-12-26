#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

from django.conf.urls import patterns, include, url
from settings import MEDIA_ROOT, STATIC_ROOT
from django.contrib import admin


urlpatterns = patterns('',
   url(r'^', include('quick.main.urls')),
   url(r'^admin/', include(admin.site.urls)),
)

# API
urlpatterns += (
    url(r'api/v1/^', include('quick.account.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
    url(r'^components/bower_components/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
)
