# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 19:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_place_max_people_capacity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='desk',
            new_name='desks',
        ),
        migrations.AddField(
            model_name='place',
            name='hours',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='max_people_capacity',
            field=models.PositiveIntegerField(choices=[(1, '1 people'), (2, '2 people'), (3, '3 people'), (4, '4 people'), (5, '5 people'), (6, '6 people'), (7, '7 people'), (8, '8 people'), (9, '9 people'), (500, '500 people'), (600, '600 people'), (700, '700 people'), (800, '800 people'), (900, '900 people'), (1000, '1000 people'), (1100, '1100 people'), (1200, '1200 people'), (1300, '1300 people'), (1400, '1400 people')], default=50),
        ),
    ]
