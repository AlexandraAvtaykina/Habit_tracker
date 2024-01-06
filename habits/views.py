from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsAutor
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    # Функция привязывает автора к его привычке
    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Просмотр одной привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitUpdateAPIView(UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitDestroyAPIView(DestroyAPIView):
    """ Удаление привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAutor]


class HabitListAPIView(ListAPIView):
    """ Список привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAutor]


class HabitPublicAPIView(ListAPIView):
    """ Список публичных привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
