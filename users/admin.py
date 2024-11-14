from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'pk',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'payment_course', 'payment_lesson', 'price', 'payment_method')
    list_filter = ('user', 'payment_date', 'payment_course', 'payment_lesson', 'price', 'payment_method')