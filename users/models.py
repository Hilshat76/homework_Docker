from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} - {self.first_name}'


class Payment(models.Model):
    class Payment_method(models.TextChoices):
        CASH = 'cash', 'Наличный расчет'
        TRANSFER = 'transfer', 'Перевод'

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(verbose_name='Дата платежа', **NULLABLE)
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name="Стоимость")
    payment_method = models.CharField(max_length=8, verbose_name="Способ оплаты", choices=Payment_method.choices,default=Payment_method.CASH)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.payment_method
