from rest_framework import serializers

from habits.models import Habit
from habits.validators import ValidateTimeHabit, ValidatorConnectionHabitAndAward, ValidatorConnectionHabit, \
    ValidatorPleasantHabit, ValidatorPeriod


class HabitSerializers (serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ValidateTimeHabit(field='time_habit'),
            ValidatorConnectionHabitAndAward(field_one='connection_habit', field_two='award'),
            ValidatorConnectionHabit(field_one='pleasant_habit', field_two='connection_habit'),
            ValidatorPleasantHabit(field_one='pleasant_habit', field_two='award', field_three='connection_habit'),
            ValidatorPeriod(field='period'),

        ]

