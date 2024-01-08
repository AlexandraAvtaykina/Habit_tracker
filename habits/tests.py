from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitApiTestCase(APITestCase):
    """ Тесты на CRUD привычек"""

    def setUp(self) -> None:
        user = User.objects.create(email='test@test.test', is_active=True)
        user.set_password('test_password')
        user.save()
        response = self.client.post(
            '/users/token/',
            data={"email": "test@test.test", "password": "test_password"})
        self.token = response.json()["access"]

        self.user = user

    def test_create_lesson(self):
        """ Тестирование создания привычки"""

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        Habit.objects.create(
            user=self.user,
            place='Тест',
            time="2024-01-01 11:42:49",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Тест'
        )

        response = self.client.post(
            '/habits/create/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Habit.objects.all().exists())

    def test_list_lesson(self):
        """ Тестирование вывода списка привычек """

        Habit.objects.create(
            user=self.user,
            place='Тест',
            time="2024-01-01 11:42:49",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Тест'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            '/habits/list/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода одной привычки"""

        habit = Habit.objects.create(
            user=self.user,
            place='Тест',
            time="2024-01-01 11:42:49",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Тест'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            f'/habits/retrieve/{habit.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """Тестирование редактирования привычки """

        habit = Habit.objects.create(
            user=self.user,
            place='Тест',
            time="2024-01-01 11:42:49",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Тест'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            'place': 'Test update'
        }

        response = self.client.patch(
            f'/habits/update/{habit.id}/',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['place'],
            'Test update'
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        habit = Habit.objects.create(
            user=self.user,
            place='Тест',
            time="2024-01-01 11:42:49",
            action='good_mood',
            is_nice=False,
            period="daily",
            lead_time=30,
            is_public=True,
            reward='Тест'
        )

        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.delete(
            f'/habits/destroy/{habit.id}/',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
