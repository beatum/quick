#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'quick.main.views.home_page'),
)