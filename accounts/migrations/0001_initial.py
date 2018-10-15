# Generated by Django 2.1.1 on 2018-10-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=40)),
                ('registerDate', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
    ]
