# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_alter_field_ip_on_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
