# Generated by Django 5.1 on 2024-09-01 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time_execution', models.TimeField(blank=True, null=True, verbose_name='Время')),
                ('action', models.CharField(max_length=300, verbose_name='Действие')),
                ('pleasant_habit', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('connection_habit', models.CharField(blank=True, max_length=300, null=True, verbose_name='Связная привычка')),
                ('period', models.DateTimeField(verbose_name='Период')),
                ('award', models.CharField(blank=True, max_length=300, null=True, verbose_name='Вознаграждение')),
                ('time_habit', models.TimeField(blank=True, null=True, verbose_name='Время на выполнение')),
                ('publication', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
