# Generated by Django 3.1.2 on 2020-11-24 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='network',
            old_name='connection',
            new_name='connections',
        ),
    ]