# Generated by Django 3.0.7 on 2020-06-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('fbid', models.CharField(max_length=255)),
                ('skill', models.CharField(max_length=255)),
                ('profile_pics', models.CharField(max_length=255)),
                ('Duration', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=255)),
                ('time_of_reminder', models.CharField(max_length=255)),
            ],
        ),
    ]
