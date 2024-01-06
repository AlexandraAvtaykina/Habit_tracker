from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView,
                          HabitRetrieveAPIView,
                          HabitDestroyAPIView,
                          HabitListAPIView,
                          HabitPublicAPIView,
                          HabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(),
         name='create_habit'),  # Создание привычки

    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(),
         name='retrieve_habit'),  # Просмотр одной привычки

    path('update/<int:pk>/', HabitUpdateAPIView.as_view(),
         name='update_habit'),  # Редактирование привычки

    path('destroy/<int:pk>/', HabitDestroyAPIView.as_view(),
         name='destroy_habit'),  # Удаление привычки

    path('list/', HabitListAPIView.as_view(),
         name='list_habit'),  # Список привычек

    path('list_public/', HabitPublicAPIView.as_view(),
         name='list_habit_public')  # Список публичных привычек
]
