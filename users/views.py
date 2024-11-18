from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.models import Payment, User
from users.permissions import IsUser
from users.serializers import PaymentSerializer, UserSerializer, UserNotOwnerSerializer


class UserCreateAPIView(CreateAPIView):
    """Создать пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Список пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """Профиль пользователя"""
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Если запрашивается свой профиль, используем полный сериализатор, иначе сокращенный сериализатор."""
        if self.request.user == self.get_object():
            return UserSerializer
        else:
            return UserNotOwnerSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Изменить пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsUser)


class UserDestroyAPIView(DestroyAPIView):
    """Удалить пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsUser)


class PaymentViewSet(ModelViewSet):
    """Позволяет автоматически реализовать стандартные методы CRUD для модели Payment"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method',)
    ordering_fields = ("payment_date",)
