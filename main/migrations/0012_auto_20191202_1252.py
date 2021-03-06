# Generated by Django 2.2.7 on 2019-12-02 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20191202_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('team', models.IntegerField()),
                ('week01', models.CharField(max_length=5)),
                ('week02', models.CharField(max_length=5)),
                ('week03', models.CharField(max_length=5)),
                ('week04', models.CharField(max_length=5)),
                ('week05', models.CharField(max_length=5)),
                ('week06', models.CharField(max_length=5)),
                ('week07', models.CharField(max_length=5)),
                ('week08', models.CharField(max_length=5)),
                ('week09', models.CharField(max_length=5)),
                ('week10', models.CharField(max_length=5)),
                ('week11', models.CharField(max_length=5)),
                ('week12', models.CharField(max_length=5)),
                ('week13', models.CharField(max_length=5)),
                ('week14', models.CharField(max_length=5)),
                ('week15', models.CharField(max_length=5)),
                ('week16', models.CharField(max_length=5)),
                ('week17', models.CharField(max_length=5)),
                ('week18', models.CharField(max_length=5)),
                ('week19', models.CharField(max_length=5)),
                ('week20', models.CharField(max_length=5)),
                ('week21', models.CharField(max_length=5)),
                ('week22', models.CharField(max_length=5)),
                ('week23', models.CharField(max_length=5)),
                ('week24', models.CharField(max_length=5)),
                ('week25', models.CharField(max_length=5)),
                ('week26', models.CharField(max_length=5)),
                ('week27', models.CharField(max_length=5)),
                ('week28', models.CharField(max_length=5)),
                ('week29', models.CharField(max_length=5)),
                ('week30', models.CharField(max_length=5)),
                ('week31', models.CharField(max_length=5)),
                ('week32', models.CharField(max_length=5)),
                ('week33', models.CharField(max_length=5)),
                ('week34', models.CharField(max_length=5)),
                ('week35', models.CharField(max_length=5)),
                ('week36', models.CharField(max_length=5)),
                ('week37', models.CharField(max_length=5)),
                ('week38', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='premierteams',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 52, 38, 342192), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 52, 38, 342192), verbose_name='date published'),
        ),
    ]
