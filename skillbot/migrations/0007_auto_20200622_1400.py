# Generated by Django 3.0.7 on 2020-06-22 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillbot', '0006_auto_20200622_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='our_user',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='our_user',
            name='date_made',
        ),
        migrations.RemoveField(
            model_name='our_user',
            name='date_made1',
        ),
    ]
