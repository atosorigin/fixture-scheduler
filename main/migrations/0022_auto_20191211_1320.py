# Generated by Django 2.2.6 on 2019-12-11 13:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20191211_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule_line_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='main.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='main.Team')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Period')),
            ],
            managers=[
                ('schedule_line_items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='PremierTeams',
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
        migrations.AlterModelManagers(
            name='schedule',
            managers=[
                ('schedules', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='home_team',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='period',
        ),
        migrations.AddField(
            model_name='schedule',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]