# Generated by Django 3.0.7 on 2020-06-28 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.DeleteModel(
            name='StudentDetail',
        ),
    ]
