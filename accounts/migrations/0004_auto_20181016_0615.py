# Generated by Django 2.1.1 on 2018-10-15 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_participate_teamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='registerDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 21, 15, 11, 691268, tzinfo=utc), verbose_name='date registered'),
        ),
    ]