# Generated by Django 2.2.6 on 2019-12-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20191211_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='league',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.League'),
            preserve_default=False,
        ),
    ]
