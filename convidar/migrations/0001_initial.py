# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('acceptation', models.BooleanField(help_text='Do you accept the invitation to come', verbose_name='acceptation')),
                ('firstname', models.CharField(max_length=50, help_text='Your Firstname', default='Your Firstname', verbose_name='firstname')),
                ('lastname', models.CharField(max_length=50, help_text='Your Lastname', default='Your Lastname', verbose_name='firstname')),
                ('telephone', models.CharField(max_length=20, help_text='Your telephone/cell number', default='000-000-0000', verbose_name='telephone_number')),
                ('accompagnement', models.PositiveIntegerField(help_text='Number of accompagnement', default=2, verbose_name='accompagnement')),
                ('notes', models.TextField(verbose_name='notes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
