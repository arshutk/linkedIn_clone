# Generated by Django 3.1.2 on 2020-11-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_delete_follow'),
        ('network', '0003_auto_20201112_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to='userauth.UserProfile'),
        ),
    ]