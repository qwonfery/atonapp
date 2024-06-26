# Generated by Django 5.0.6 on 2024-06-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(default='fullname', max_length=50, verbose_name='ФИО')),
                ('username', models.CharField(default='username', max_length=50, unique=True, verbose_name='Логин')),
                ('password', models.CharField(default='password', max_length=50, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
