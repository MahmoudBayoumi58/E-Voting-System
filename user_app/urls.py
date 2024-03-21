from django.urls import path
from .views import *

urlpatterns = [
    path('login', user_login, name='login'),
    path('register', register, name='register'),
    path('activate/<str:code>/', activate_account, name='activate'),
    path('forget-password', forget_password, name='forget_password'),
    path('dashboard', dashboard, name='dashboard'),
    path('error_404', error_404, name='error_404'),
    path('error_401', error_401, name='error_401'),
    path('error_500', error_500, name='error_500'),
]
