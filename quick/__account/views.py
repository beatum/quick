#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

from rest_framework import permissions
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    Allow only authorized users allow view, but only owner can modify existing
    instances. TODO: Delete method must be excluded!
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer