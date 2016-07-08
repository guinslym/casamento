from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Reservation
from .forms import (
        ReservationCrispyFormModelForm,
        ReservationDjangoBootstrapFormModelForm
        )
# Create your views here.

class ReservationCreateView(CreateView):
    """use crispy_forms """
    form_class = ReservationCrispyFormModelForm
    success_url =  '/'
    template_name = '_create.html'

    def form_valid(self, form):
        return super(ReservationCreateView, self).form_valid(form)


class Reservation2CreateView(CreateView):
    form_class = ReservationDjangoBootstrapFormModelForm
    success_url =  '/'
    template_name = 'bootstrap.html'

    def form_valid(self, form):
        return super(Reservation2CreateView, self).form_valid(form)

class Reservation3CreateView(CreateView):
    """use crispy_forms """
    form_class = ReservationCrispyFormModelFormWithHelperTextAndLabels
    success_url =  '/'
    template_name = '_create.html'

    def form_valid(self, form):
        return super(Reservation3CreateView, self).form_valid(form)
