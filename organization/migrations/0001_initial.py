# Generated by Django 3.1.2 on 2020-11-12 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('is_remote', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=50)),
                ('employement_type', models.CharField(choices=[('Fulltime', 'Full-Time'), ('Parttime', 'Part-Time'), ('Internship', 'Internship'), ('Contract', 'Contract')], default=None, max_length=50)),
                ('description', models.TextField()),
                ('file_linked', models.FileField(blank=True, max_length=1048576, null=True, upload_to='organisation/jobs')),
                ('skills_required', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Test Score',
                'verbose_name_plural': 'Test Scores',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('headquarter', models.CharField(max_length=50)),
                ('website_url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='OrganizationStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.userprofile')),
                ('oganization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='organization.organization')),
                ('page_admins', models.ManyToManyField(blank=True, related_name='admin_of_pages', to='userauth.UserProfile')),
                ('page_superadmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superadmin_of_pages', to='userauth.userprofile')),
            ],
            options={
                'verbose_name': 'Organization Staff',
                'verbose_name_plural': 'Organization Staff',
            },
        ),
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('tagline', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, max_length=1048576, null=True, upload_to='organization/logo')),
                ('oganization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='organization.organization')),
            ],
            options={
                'verbose_name': 'Organization Profile',
                'verbose_name_plural': 'Organization Profiles',
            },
        ),
        migrations.CreateModel(
            name='OrganizationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_industry', models.CharField(choices=[('Accounting', 'Accounting'), ('Aviation', 'Aviation'), ('Animation', 'Animation'), ('Architecture', 'Architecture'), ('Arts and Craft', 'Arts and Craft'), ('Biotechnology', 'Biotechnology'), ('Civil Engineering', 'Civil Engineering'), ('Computer Network', 'Computer Network'), ('Computer Hardware', 'Computer Hardware'), ('Computer Software', 'Computer Software'), ('Education', 'Education'), ('Pharmaceutical', 'Pharmaceutical')], default=None, max_length=50)),
                ('organization_size', models.CharField(choices=[('10', '1-10'), ('50', '10-50'), ('100', '50-100'), ('500', '100-500'), ('1000', '500-1000'), ('5000', '1000-5000'), ('10000', '5000-10000'), ('10000', '10000+')], default=None, max_length=50)),
                ('organization_type', models.CharField(choices=[('Public', 'Public'), ('Government', 'Government'), ('Private', 'Private'), ('Nonprofit', 'Nonprofit')], default=None, max_length=50)),
                ('oganization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='organization.organization')),
            ],
            options={
                'verbose_name': 'Organization Detail',
                'verbose_name_plural': 'Organization Details',
            },
        ),
        migrations.CreateModel(
            name='OrganizationAnalytic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oganization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_by', to='organization.organization')),
                ('viewed_by', models.ManyToManyField(blank=True, to='userauth.UserProfile')),
            ],
            options={
                'verbose_name': 'Organization Analytic',
                'verbose_name_plural': 'Organization Analytics',
            },
        ),
        migrations.CreateModel(
            name='JobVacancyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_questions', to='organization.jobvacancy')),
            ],
        ),
        migrations.AddField(
            model_name='jobvacancy',
            name='oganization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='organization.organization'),
        ),
    ]
