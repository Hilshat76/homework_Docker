from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "user",
            "payment_date",
            "payment_course",
            "payment_lesson",
            "price",
            "payment_method",
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserNotOwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "date_joined")
