from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Reservation
from .forms import ReservationForm
# Create your views here.

class ReservationCreateView(CreateView):
    model = Author
    fields = ['name']
