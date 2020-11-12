# Generated by Django 3.1.2 on 2020-11-12 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_delete_follow'),
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(blank=True, related_name='_follow_followers_+', to='network.Follow')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='userauth.userprofile')),
            ],
        ),
    ]
