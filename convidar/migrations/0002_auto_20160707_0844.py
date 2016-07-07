# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='acceptation',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], verbose_name='acceptation', help_text='Do you accept the invitation to come', max_length=10),
        ),
    ]
