# Generated by Django 2.2.6 on 2019-12-11 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20191203_0756'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClubPairings',
        ),
        migrations.DeleteModel(
            name='DateRequests',
        ),
        migrations.AlterField(
            model_name='premierteams',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 10, 24, 6, 358002), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 10, 24, 6, 357002), verbose_name='date published'),
        ),
    ]
