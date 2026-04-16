from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='admin_home'),
    path('panel/', panel, name='panel'),
    path('registro/', register_user, name='register_user'),
    path('api/mobile/register/', mobile_register, name='mobile_register'),
    path('api/mobile/login/', mobile_login, name='mobile_login'),
    path('api/jwt/login/', jwt_login, name='jwt_login'),
]