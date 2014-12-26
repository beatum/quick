
#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

# from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register(r'account', UserViewSet)
urlpatterns = router.urls


# urlpatterns = (
#     url(r'^', include(router.urls)),
# )