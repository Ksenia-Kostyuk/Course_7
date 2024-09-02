from datetime import timedelta, datetime

from rest_framework.exceptions import ValidationError


class ValidateTimeHabit:
    """Проверяет, что время на выполнение привычке равно менее 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value in self.field > timedelta(seconds=120):
            raise ValidationError('Время выполнения привычки не может превышать 2 минут')


class ValidatorConnectionHabitAndAward:
    """Проверяет заполнены ли поля вознаграждения и связной привычке одновременно,
    если да возбуждает ошибку"""

    def __init__(self, field_one, field_two):
        self.field_one = field_one
        self.field_two = field_two

    def __call__(self):
        if self.field_one is True and self.field_two is True:
            raise ValidationError('Это связная привычка или вознаграждение? Выберите что-то одно!')


class ValidatorConnectionHabit:
    """Проверяет являются ли связные привычки приятными"""

    def __init__(self, field_one, field_two):
        self.field_one = field_one
        self.field_two = field_two

    def __call__(self):
        if self.field_one is True and self.field_two is False:
            raise ValidationError('Связными привычками могут быть только приятные привычки')
        elif self.field_one is False and self.field_two is True:
            raise ValidationError('Укажите привычку, как связную')


class ValidatorPleasantHabit:
    """Проверяет приятная ли привычка, при наличии вознаграждения
    или связной привычки возбуждает ошибку"""

    def __init__(self, field_one, field_two, field_three):
        self.field_one = field_one
        self.field_two = field_two
        self.field_three = field_three

    def __call__(self):
        match True:
            case self.field_one|self.field_two|self.field_three: raise ValidationError('Укажите привычку, как связную')


class ValidatorPeriod:
    """Проверяет выполняется ли привычка не реже 1 раза в неделю"""

    def __init__(self, field):
        self.field = field

    def __call__(self):
        difference = self.field - datetime.now()
        if difference > timedelta(days=7):
            raise ValidationError('Привычку нельзя не выполнять более 7 дней')

