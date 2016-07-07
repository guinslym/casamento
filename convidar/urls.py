
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^create/$', 'convidar.views.ReservationCreateView', name="add_invitation"),
    url(r'^$',
        TemplateView.as_view(template_name='hello.html'),
        name="add_invitation"),

)
