# Generated by Django 2.1.2 on 2018-10-28 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamproject', '0003_team_peoplenum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='peopleNum',
        ),
    ]