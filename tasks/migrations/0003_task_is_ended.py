# Generated by Django 3.1.1 on 2020-09-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200908_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_ended',
            field=models.BooleanField(default=False),
        ),
    ]
