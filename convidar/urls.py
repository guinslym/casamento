
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import (
    ReservationCreateView,
    bootstrap,
    Reservation3CreateView
)
urlpatterns = patterns('',
    url(r'^create/$', ReservationCreateView.as_view(), name='create'),
    url(r'^bootstrap/$', bootstrap, name='bootstrap'),
    url(r'^create2/$', Reservation3CreateView.as_view(), name='create2'),
    url(r'^$', 'convidar.views.message_to_user', name="message_to_user"),
    url(r'^done/$',
        'django.shortcuts.render',
        {'template_name': "message_to_user_done.html"},
        name="message_to_user_done"
        ),
    url(r'^$',
        TemplateView.as_view(template_name='hello.html'),
        name="add_invitation"),

)
