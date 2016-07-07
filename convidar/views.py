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
    form_class = ReservationCrispyFormModelForm
    success_url =  '/'
    template_name = '_create.html'

    def form_valid(self, form):
        return super(ReservationCreateView, self).form_valid(form)

def bootstrap(request):
    form = ReservationDjangoBootstrapFormModelForm()

    return render(request, 'bootstrap.html', {'form': form})
