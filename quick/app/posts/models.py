#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 28.12.14.
"""

from django.db import models
from quick.user.models import Account


class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.content)