# Generated by Django 3.2.7 on 2021-09-16 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagnikapp', '0002_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('bmi', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 9, 16, 17, 46, 33, 546047))),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 17, 46, 33, 546047)),
        ),
    ]
