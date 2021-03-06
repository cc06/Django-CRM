# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
        ('common', '0001_initial'),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='assigned_to',
            field=models.ManyToManyField(related_name='case_assigned_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='contacts',
            field=models.ManyToManyField(to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='teams',
            field=models.ManyToManyField(to='common.Team'),
        ),
    ]
