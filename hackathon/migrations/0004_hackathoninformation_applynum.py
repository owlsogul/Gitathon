# Generated by Django 2.1.2 on 2018-10-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_hackathoninformation_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathoninformation',
            name='applyNum',
            field=models.IntegerField(default=0),
        ),
    ]