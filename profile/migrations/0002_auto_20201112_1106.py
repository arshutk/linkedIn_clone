# Generated by Django 3.1.2 on 2020-11-12 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skills',
            new_name='skills_list',
        ),
    ]
