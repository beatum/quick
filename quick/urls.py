#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""
from django.contrib import admin

from django.conf.urls import include, patterns, url
from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet
from main.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(router, r'accounts',
                                             lookup='account')
accounts_router.register(r'posts', AccountPostsViewSet)


urlpatterns = patterns(
    '',

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', IndexView.as_view(), name='index'),
)


from settings import MEDIA_ROOT, STATIC_ROOT
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
