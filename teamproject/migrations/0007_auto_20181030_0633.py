# Generated by Django 2.1.1 on 2018-10-29 21:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teamproject', '0006_auto_20181030_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamnotice',
            name='writtenDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 21, 33, 58, 488949, tzinfo=utc), verbose_name='date registered'),
        ),
    ]
