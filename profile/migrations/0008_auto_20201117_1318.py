# Generated by Django 3.1.2 on 2020-11-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0007_auto_20201117_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobvacancy',
            name='payscale',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
