#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""
from django.views.generic.base import TemplateResponse
from django.utils.translation import ugettext


def home_page(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    return TemplateResponse(request, 'page/home_page.html',
                            {'message': message})