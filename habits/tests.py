from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.habit = Habit.objects.create(owner=self.user, place='Улица', action='Пробежка', pleasant_habit=False,
                                          award='Сон', publication=False)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse('habits:habits-create')
        data = {
            "owner": self.user.pk,
            "place": self.habit.place,
            "action": self.habit.action,
            "award": self.habit.award
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habits_list(self):
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_retrieve(self):
        url = reverse('habits:habits-retrieve', args=(self.habits.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habits_delete(self):
        url = reverse('habits:habits-delete', args=(self.habits.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
