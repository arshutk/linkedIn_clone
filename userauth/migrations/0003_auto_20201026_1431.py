# Generated by Django 3.1.2 on 2020-10-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20201026_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexperience',
            name='end_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]