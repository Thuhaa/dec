# Generated by Django 3.1.4 on 2020-12-18 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='DataFile',
        ),
    ]
