# Generated by Django 3.1.2 on 2020-11-16 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobvacancyquestion',
            name='organization',
        ),
        migrations.DeleteModel(
            name='JobVacancy',
        ),
        migrations.DeleteModel(
            name='JobVacancyQuestion',
        ),
    ]
