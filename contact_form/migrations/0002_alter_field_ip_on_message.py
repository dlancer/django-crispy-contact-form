# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='ip',
            field=models.GenericIPAddressField(null=True, verbose_name='IP', blank=True),
        ),
    ]
