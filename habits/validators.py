from rest_framework.serializers import ValidationError

from habits.models import Habit


class HabitValidator:
    """ Исключить одновременный выбор
    связанной привычки и указания вознаграждения """

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        val2 = dict(value).get(self.field2)
        if val1 and val2:
            raise ValidationError("Нельзя одновременно выбирать"
                                  " связанную привычку и вознаграждение!")


class TimeValidator:
    """ Время выполнения должно быть не больше 120 секунд """

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val = dict(value).get(self.field1)
        if val is not None and int(val) > 120:
            raise ValidationError("Время больше 120 секунд!")


class ConnectedHabitValidator:
    """ В связанные привычки могут попадать
    только привычки с признаком приятной привычки """

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        filter_list = list(Habit.objects.filter(is_nice=False).values())
        for i in filter_list:
            if val1 is not None:
                if i['id'] == val1.id:
                    raise (ValidationError
                           ("В связанные привычки могут попадать"
                            " только привычки с признаком приятной привычки"))


class NiceHabitValidator:
    """ У приятной привычки не может быть
     вознаграждения или связанной привычки """

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        val2 = dict(value).get(self.field2)
        val3 = dict(value).get(self.field3)
        if val1 is True and (val2 is not None or val3 is not None):
            raise (ValidationError
                   ("У приятной привычки не может"
                    " быть вознаграждения или связанной привычки"))
