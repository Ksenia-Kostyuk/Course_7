from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import CustomHabitPagination
from habits.serializers import HabitSerializers
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    pagination_class = CustomHabitPagination

    def get_queryset(self, request, queryset):
        if request.user.is_authenticated:
            return queryset.filter(publication=True)
        elif request.user.is_authenticated is False:
            raise AuthenticationFailed('Вам необходимо зарегистрироваться')
        else:
            return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = (IsAuthenticated, IsOwner,)

