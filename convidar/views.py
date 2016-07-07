from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Reservation
from .forms import ReservationForm
# Create your views here.

class ReservationCreateView(CreateView):
    form_class = ReservationForm
    success_url =  '/'
    template_name_suffix = '_create'

    def form_valid(self, form):
        return super(ReservationCreateView, self).form_valid(form)
