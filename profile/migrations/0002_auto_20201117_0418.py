# Generated by Django 3.1.2 on 2020-11-16 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobvacancy',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_posted', to='userauth.userprofile'),
        ),
    ]
