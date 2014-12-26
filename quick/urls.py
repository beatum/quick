#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from account import views
from rest_framework.routers import DefaultRouter
# from account.views import UserViewSet


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
)
