from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # Получение токена
    path('create_user/', UserCreateAPIView.as_view(),
         name='create_user')  # Создание пользователя
]
