# Generated by Django 4.2.2 on 2023-06-28 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pick_em', '0002_alter_team_team_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='schedule_season',
        ),
    ]
