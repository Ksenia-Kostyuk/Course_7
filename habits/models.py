from django.db import models


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')
    place = models.CharField(max_length=150, verbose_name='Место')
    time_execution = models.TimeField(blank=True, null=True, verbose_name='Время')
    action = models.CharField(max_length=300, verbose_name='Место')
    pleasant_habit = models.BooleanField(default=True, verbose_name='Признак полезной привычки')
    connection_habit = models.CharField(blank=True, null=True, max_length=150, verbose_name='Место')
    period = models.DateTimeField(verbose_name='Период')
    award = models.CharField(max_length=300, blank=True, null=True, verbose_name='Вознаграждение')
    time_habit = models.TimeField(blank=True, null=True, verbose_name='Время на выполнение')
    publication = models.BooleanField(default=False, verbose_name='Признак публикации')

