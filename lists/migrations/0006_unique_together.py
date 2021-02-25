# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-25 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_remove_duplicates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
