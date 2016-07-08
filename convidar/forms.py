from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import layout
from crispy_forms.bootstrap import Field, FormActions

#from captcha.fields import ReCaptchaField


class ReservationCrispyFormModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["acceptation", "firstname", "lastname",
                "telephone", "accompagnement", "notes"]

    def __init__(self, *args, **kwargs):
        super(ReservationCrispyFormModelForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-4'
        self.fields["acceptation"].widget = forms.RadioSelect()
        # delete empty choice for the type
        del self.fields["acceptation"].choices[0]
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                Field("acceptation", css_class="input-block-level"),
                _("Renseignement"),
                Field("firstname", css_class="input-block-level"),
                Field("lastname", css_class="input-block-level"),
                Field("telephone", css_class="input-block-level"),
                Field("accompagnement", css_class="input-block-level"),
                Field("notes", css_class="input-block-level", rows="3"),
                ),
                FormActions(
                    Submit("submit", _("Save")),
                )
        )



from django.forms import ModelForm, EmailInput

class ReservationDjangoBootstrapFormModelForm(forms.Form):
    firstname = forms.CharField(help_text="Your Firstname")
    lastname = forms.CharField()
    email = forms.EmailField(
            label=_("Email"),
            max_length=254,
            required=True,
            help_text="Example: your_email@gmail.com",
            widget=EmailInput(attrs={
                                 "type": "email",
                                 "id": "id_email",
                                 "autofocus": "true",
                                 "placeholder": "Email Address",
                                 "required": 'true'
            }))
    #accompagnement = forms.ChoiceField(choices=CHOICES)
    #radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    #multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    #multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    notes = forms.CharField(widget=forms.Textarea,required=True)
    acceptation = forms.BooleanField(help_text=_("Do you accept the invitation to come"))

    def clean_notes(self): #system auto looks for method starting with clean_ !
        notes=self.cleaned_data['notes']
        num_words=len(notes.split())
        if num_words<10:
            raise forms.ValidationError('''Not enough words.
                Enter atleast 10 words''')

        return notes #Returns the same message so that we could modify it.


class ReservationCrispyFormModelFormWithHelperTextAndLabels(ModelForm):
    """
        Don't really looks at the content like 'If you disable this, Kaniwani..'
        The most important thing is the use of 'help_texts' and 'labels'
    """
    class Meta:
        model = Reservation
        fields = ["acceptation", "firstname", "lastname",
                "telephone", "accompagnement", "notes"]
        help_texts = {
            "acceptation": ("If you disable this, Kaniwani will no longer automatically unlock things as you unlock them in Wanikani."),
            "telephone": ("Enabling this setting will prevent your reviews from accumulating.")
        }
        labels = {
            "acceptation": "Follow Wanikani Progress",
            "telephone": "Automatically advance to next item in review if answer was correct.",
            "firstname": "Automatically show kanji and kana if you answer correctly.",
            "lastname": "Automatically show kanji and kana if you answer incorrectly.",
            "accompagnement": "Review only items that you have burned in Wanikani.",
            "notes": "Vacation Mode"
        }
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_id = 'ReservationCrispyFormModelFormWithHelperTextAndLabels'
        self.helper.form_class = 'settings-form pure-form pure-form-stacked'
        self.helper.add_input(Submit("submit", "Save", css_class='pure-button pure-button-primary'))
        self.helper.label_class = ''
        self.helper.field_class = 'pure-input-1'
        self.helper.form_style = "default"
        self.helper.help_text_inline = False
        self.helper.error_text_inline = False
        super(ReservationCrispyFormModelFormWithHelperTextAndLabels, self).__init__(*args, **kwargs)
        #self.fields['level'].widget.attrs['readonly'] = True
        #self.fields['level'].disabled = True

    def clean_api_key(self):
        api_key = self.cleaned_data['api_key']
        r = requests.get("https://www.wanikani.com/api/user/{}/user-information".format(api_key))
        if r.status_code == 200:
            json_data = r.json()
            if "error" in json_data.keys():
                raise ValidationError("API Key not associated with a WaniKani User!")
        print("cleaned api Key...")
        return api_key
