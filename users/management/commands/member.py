import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Создание обычного пользователя """

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='alexandra@mail.ru',
            chat_id=os.getenv("CHAT_ID_MEMBER"),
            first_name='neAdmin',
            last_name='neAdminov',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password('123qwe456rty')
        user.save()
