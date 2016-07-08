from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Reservation
from .forms import (
        ReservationCrispyFormModelForm,
        ReservationDjangoBootstrapFormModelForm,
        ReservationCrispyFormModelFormWithHelperTextAndLabels,
        MessageForm
        )


class ReservationCreateView(CreateView):
    form_class = ReservationCrispyFormModelForm
    success_url =  '/'
    template_name = '_create.html'

    def form_valid(self, form):
        return super(ReservationCreateView, self).form_valid(form)
##################################
##################################
##################################

def bootstrap(request):
    form = ReservationDjangoBootstrapFormModelForm()

    return render(request, 'bootstrap.html', {'form': form})
#############################################
#############################################
#############################################


class Reservation3CreateView(CreateView):
    form_class = ReservationCrispyFormModelFormWithHelperTextAndLabels
    success_url =  '/'
    template_name = '_create.html'

    def form_valid(self, form):
        return super(Reservation3CreateView, self).form_valid(form)

##################################
##################################
##################################

def message_to_user(request):
    if request.method == "POST":
        form = MessageForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("message_to_user_done")
    else:
        form = MessageForm(request)

    return render(request, "message_to_user.html", {"form": form})

#############################################
#############################################
#############################################

from .forms import BulletinForm


def add_bulletin(request):
    """
        Dummy view to show the form with layout
    """
    form = BulletinForm()
    return render(request, "change_bulletin.html", {'form': form})
