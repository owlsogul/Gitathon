# Generated by Django 2.1.2 on 2018-10-29 22:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20181030_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='registerDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 22, 36, 38, 533804, tzinfo=utc), verbose_name='date registered'),
        ),
        migrations.AlterField(
            model_name='participate',
            name='hackId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hackathon.HackathonInformation'),
        ),
    ]