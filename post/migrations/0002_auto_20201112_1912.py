# Generated by Django 3.1.2 on 2020-11-12 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_userprofile_followers'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='wriiten_by',
        ),
        migrations.AddField(
            model_name='post',
            name='written_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='writiten_by', to='userauth.userprofile'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('celebrate', models.IntegerField(default=0)),
                ('support', models.IntegerField(default=0)),
                ('love', models.IntegerField(default=0)),
                ('insightful', models.IntegerField(default=0)),
                ('curious', models.IntegerField(default=0)),
                ('downvoter', models.ManyToManyField(blank=True, related_name='downvoter', to='userauth.UserProfile')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='post.post')),
                ('upvoter', models.ManyToManyField(blank=True, related_name='upvoter', to='userauth.UserProfile')),
            ],
            options={
                'ordering': ('-like', '-celebrate', '-support', '-love', '-insightful', '-curious'),
            },
        ),
    ]
