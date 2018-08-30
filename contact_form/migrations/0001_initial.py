# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=80, verbose_name='Sender name')),
                ('sender_email', models.EmailField(max_length=254, verbose_name='Sender email')),
                ('message', models.TextField(max_length=4096, verbose_name='Message')),
                ('ip', models.IPAddressField(null=True, verbose_name='IP', blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('department', models.ForeignKey(to='contact_form.Department', on_delete=models.CASCADE)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.ForeignKey(verbose_name='Subject', to='contact_form.Subject', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
