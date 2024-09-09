from django.urls import path

from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

router = SimpleRouter()

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('list/', HabitListAPIView.as_view(), name='habits-list'),
    path('detail/', HabitRetrieveAPIView.as_view(), name='habits-detail'),
    path('update/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('delete/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]
