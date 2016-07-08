from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Reservation(TimeStampedModel):
    """
    """
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        pass#return reverse('delivrem:detail', args=(self.id,))

    TYPE_CHOICES = (
        ('Oui', _("Oui")),
        ('Non', _("Non")),
    )

    acceptation = models.CharField(_("acceptation"),
                            max_length=10,
                            help_text=_("Do you accept the invitation to come"),
                            choices=TYPE_CHOICES)
    firstname = models.CharField(_("firstname"),
                        help_text=_("Your Firstname"),
                        max_length=50,
                        default="Your Firstname")
    lastname = models.CharField(_("lastname"),
                        help_text=_("Your Lastname"),
                        max_length=50,
                        default="Your Lastname")
    telephone =  models.CharField(_("telephone_number"),
                        help_text=_("Your telephone/cell number"),
                         max_length=20,
                        default="000-000-0000")
    accompagnement = models.PositiveIntegerField(_("accompagnement"),
                        help_text=_("Number of accompagnement"),
                        default=2
                        )
    notes = models.TextField(_("notes"))


#######################################################
#######################################################
#######################################################
#######################################################
#######################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

TYPE_CHOICES = (
    ('searching', _("Searching")),
    ('offering', _("Offering")),
)

@python_2_unicode_compatible
class Bulletin(models.Model):
    bulletin_type = models.CharField(_("Type"), max_length=20, choices=TYPE_CHOICES)

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), max_length=300)

    contact_person = models.CharField(_("Contact person"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=200, blank=True)
    email = models.EmailField(_("Email"), blank=True)

    image = models.ImageField(_("Image"), max_length=255, upload_to="bulletin_board/", blank=True)

    class Meta:
        verbose_name = _("Bulletin")
        verbose_name_plural = _("Bulletins")
        ordering = ("title",)

    def __str__(self):
        return self.title
