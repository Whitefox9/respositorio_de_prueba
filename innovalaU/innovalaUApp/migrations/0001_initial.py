# Generated by Django 3.2.8 on 2021-10-10 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_estudiante',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombresEstudiante', models.CharField(max_length=50, unique=True, verbose_name='Nombres Estudiante')),
                ('apellidosEstudiante', models.CharField(max_length=50, unique=True, verbose_name='Apellidos Estudiante')),
                ('edadEstudiante', models.IntegerField(default=18)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutoria',
            fields=[
                ('idTutoria', models.AutoField(primary_key=True, serialize=False)),
                ('fechaTutoria', models.DateTimeField()),
                ('calificacionTutoria', models.IntegerField(default=0)),
                ('estudianteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudianteID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
