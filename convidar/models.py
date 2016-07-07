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
    lastname = models.CharField(_("firstname"),
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
