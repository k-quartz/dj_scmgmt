# Generated by Django 3.0.7 on 2020-07-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='stand',
            field=models.CharField(default='', max_length=10),
        ),
    ]
