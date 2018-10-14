# Generated by Django 2.1.2 on 2018-10-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0013_auto_20181014_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathoninformation',
            name='contestDate_end',
            field=models.DateField(help_text='Please use the following format : <em>YYYY-MM-DD</em>'),
        ),
        migrations.AlterField(
            model_name='hackathoninformation',
            name='contestDate_start',
            field=models.DateField(help_text='Please use the following format : <em>YYYY-MM-DD</em>'),
        ),
        migrations.AlterField(
            model_name='hackathoninformation',
            name='contestTime_end',
            field=models.TimeField(help_text='Please use the following format : <em>12:00:00</em>'),
        ),
        migrations.AlterField(
            model_name='hackathoninformation',
            name='contestTime_start',
            field=models.TimeField(help_text='Please use the following format : <em>12:00:00</em>'),
        ),
    ]
