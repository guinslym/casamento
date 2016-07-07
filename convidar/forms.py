from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import bootstrap, Field, layout

class ReservationForm(forms.Form):
    class Meta:
        model = Reservation
        fields = ["acceptation", "firstname", "lastname",
                "telephone", "accompagnement", "notes"]

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.fields["acceptation"].widget = forms.RadioSelect()
        # delete empty choice for the type
        del self.fields["acceptation"].choices[0]

        self.helper.layout = Layout(
                    'acceptation',
                    'firstname',
                    'lastname',
                    'telephone',
                    'accompagnement',
                    'notes',
                    ButtonHolder(
                            Submit('reservation', 'Reservation',
                            css_class='btn-primary')
                        )
                )
