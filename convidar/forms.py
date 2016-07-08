from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import layout
from crispy_forms.bootstrap import Field, FormActions



#from captcha.fields import ReCaptchaField
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################


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
                    Button('cancel', 'Cancelar', onclick="window.location.href='/';")
                )
        )

###########################################################
###########################################################
###########################################################
###########################################################
###########################################################

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
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################

class ReservationCrispyFormModelFormWithHelperTextAndLabels(forms.Form):
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

######################################################
######################################################
######################################################
######################################################
######################################################
######################################################



from django.core.mail import send_mail
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    """
    The important is the 'save method' pour alléger le View
    """
    recipient = forms.ModelChoiceField(
        label=_("Recipient"),
        queryset=User.objects.all(),
        required=True,
    )
    message = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea,
        required=True,
    )

    def __init__(self, request, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.request = request
        #we exclude the current user because of the ModelChoiceField
        #queryset=User.objects.all(),
        self.fields["recipient"].queryset = self.fields["recipient"].queryset.exclude(pk=request.user.pk)

    def save(self):
        cleaned_data = self.cleaned_data
        send_mail(
            subject=ugettext("A message from %s") % self.request.user,
            message=cleaned_data["message"],
            from_email=self.request.user.email,
            recipient_list=[cleaned_data["recipient"].email],
            fail_silently=True,
        )

#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################

from .models import Bulletin
from crispy_forms import layout, bootstrap
from captcha.fields import ReCaptchaField

class BulletinForm(forms.ModelForm):
    """
    this one is almost the same as ReservationCrispyFormModelForm
    but it uses Image upload
    """
    class Meta:
        model = Bulletin
        fields = ["bulletin_type", "title", "description", "contact_person", "phone", "email", "image"]

    #this didn't work make be my google accreditation is not valid
    captcha = ReCaptchaField(label=_('Antirobot'),required=True)
    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        #captcha = ReCaptchaField()

        self.fields["bulletin_type"].widget = forms.RadioSelect()
        # delete empty choice for the type
        del self.fields["bulletin_type"].choices[0]
        #self.fields['bulletin_type'].label = "Bulletin Type"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                layout.Field("bulletin_type"),
                layout.Field("title", css_class="input-block-level"),
                layout.Field("description", css_class="input-block-level", rows="3"),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("image", css_class="input-block-level"),
                layout.HTML(u"""{% load i18n %}
                    <p class="help-block">{% trans "Available formats are JPG, GIF, and PNG. Minimal size is 800 × 800 px." %}</p>
                """),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            layout.Fieldset(
                _("Contact"),
                layout.Field("contact_person", css_class="input-block-level"),
                layout.Div(
                    bootstrap.PrependedText("phone", """<span class="glyphicon glyphicon-earphone"></span>""", css_class="input-block-level"),
                    bootstrap.PrependedText("email", "@", css_class="input-block-level", placeholder="contact@example.com"),
                    css_id="contact_info",
                ),
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save")),
            )
        )
#####################################
#####################################
#####################################
#####################################
#####################################

from bootstrap3_datetime.widgets import DateTimePicker

class ToDoForm(forms.Form):
    """
    This form doesn't have a View nor a urls.py
    """
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    reminder = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))
