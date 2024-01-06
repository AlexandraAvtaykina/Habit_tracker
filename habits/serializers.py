from rest_framework import serializers

from habits.models import Habit
from habits.validators import (HabitValidator,
                               TimeValidator,
                               ConnectedHabitValidator,
                               NiceHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(field1='reward', field2='habits'),
                      TimeValidator(field1='lead_time'),
                      ConnectedHabitValidator(field1='habits'),
                      NiceHabitValidator(field1='is_nice',
                                         field2='reward',
                                         field3='habits')]
