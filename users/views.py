from django.utils.decorators import method_decorator
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema


from users.models import User
from users.serializers import UserSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"
))
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
