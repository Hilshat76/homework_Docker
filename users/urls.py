from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('profile/', ProfileAPIView.as_view(), name='profile'),

]
