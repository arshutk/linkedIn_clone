# Generated by Django 3.1.2 on 2020-11-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20201125_1030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trending',
            new_name='Hashtag',
        ),
    ]
