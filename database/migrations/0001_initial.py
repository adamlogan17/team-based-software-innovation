# Generated by Django 3.2.23 on 2023-11-18 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('careerID', models.AutoField(primary_key=True, serialize=False)),
                ('jobTitle', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('jobDescription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('moduleID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('moduleName', models.CharField(max_length=100)),
                ('moduleSemester', models.IntegerField(default=3)),
                ('moduleDescription', models.CharField(max_length=2500)),
                ('moduleLevel', models.IntegerField(default=1)),
                ('moduleWeight', models.IntegerField(default=20)),
                ('careers', models.ManyToManyField(blank=True, to='database.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('pathwayID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pathwayName', models.CharField(max_length=100)),
                ('pathwayLevels', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('studentCurrentLevel', models.IntegerField(default=1)),
                ('studentCurrentSemester', models.IntegerField(default=1)),
                ('currentPathwayMark', models.FloatField(default=0, editable=False)),
                ('pathwayID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.pathway')),
            ],
        ),
        migrations.CreateModel(
            name='ModulePathway',
            fields=[
                ('modulePathwayID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('mpCore', models.BooleanField(default=True)),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
                ('pathwayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.pathway')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecturerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('lecturerName', models.CharField(default='name', max_length=100)),
                ('lecturerEmail', models.EmailField(max_length=254)),
                ('lecturerModules', models.ManyToManyField(to='database.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessmentID', models.CharField(auto_created=True, max_length=8, primary_key=True, serialize=False)),
                ('assessmentType', models.CharField(max_length=20)),
                ('assessmentWeight', models.FloatField(default=20)),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=30)),
                ('addressId', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]