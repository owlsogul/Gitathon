# Generated by Django 2.1.1 on 2018-10-29 21:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teamproject', '0005_teamcontribution_teamnotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamnotice',
            name='writtenDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 21, 31, 40, 38214, tzinfo=utc), verbose_name='date registered'),
        ),
    ]