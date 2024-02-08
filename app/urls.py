from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('home/', home, name='home'),
]
