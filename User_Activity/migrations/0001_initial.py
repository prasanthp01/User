# Generated by Django 3.0.5 on 2020-07-04 09:58

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAct',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=50, verbose_name='id')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('real_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('list_act', jsonfield.fields.JSONField(default=[], verbose_name='activity_periods')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
