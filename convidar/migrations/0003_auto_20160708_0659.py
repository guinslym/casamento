# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidar', '0002_auto_20160707_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('bulletin_type', models.CharField(verbose_name='Type', choices=[('searching', 'Searching'), ('offering', 'Offering')], max_length=20)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('description', models.TextField(verbose_name='Description', max_length=300)),
                ('contact_person', models.CharField(verbose_name='Contact person', max_length=255)),
                ('phone', models.CharField(verbose_name='Phone', blank=True, max_length=200)),
                ('email', models.EmailField(verbose_name='Email', blank=True, max_length=254)),
                ('image', models.ImageField(verbose_name='Image', blank=True, max_length=255, upload_to='bulletin_board/')),
            ],
            options={
                'verbose_name': 'Bulletin',
                'verbose_name_plural': 'Bulletins',
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='reservation',
            name='lastname',
            field=models.CharField(help_text='Your Lastname', default='Your Lastname', verbose_name='lastname', max_length=50),
        ),
    ]
