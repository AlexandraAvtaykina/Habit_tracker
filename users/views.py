from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer
