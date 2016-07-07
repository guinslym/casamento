from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import layout
from crispy_forms.bootstrap import Field, FormActions


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["acceptation", "firstname", "lastname",
                "telephone", "accompagnement", "notes"]

    def __init__(self, *args, **kwargs):
        super(ReservationForm,self).__init__(*args, **kwargs)


        self.helper = FormHelper(self)
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.fields["acceptation"].widget = forms.RadioSelect()
        # delete empty choice for the type
        del self.fields["acceptation"].choices[0]

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                layout.Field("acceptation", css_class="input-block-level"),
                _("Renseignement"),
                layout.Field("firstname", css_class="input-block-level"),
                layout.Field("lastname", css_class="input-block-level"),
                layout.Field("telephone", css_class="input-block-level"),
                layout.Field("accompagnement", css_class="input-block-level"),
                layout.Field("notes", css_class="input-block-level", rows="3"),
            ),
            FormActions(
                layout.Submit("submit", _("Save")),
            )
        )


'''
class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('email', css_class='input-small', type='email'),
            FormActions(Submit('submit', 'Submit'))
        )
'''
