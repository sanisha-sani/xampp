# Generated by Django 4.0 on 2021-12-29 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_new_new1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new1',
            old_name='dob',
            new_name='lname',
        ),
    ]
