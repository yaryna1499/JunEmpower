from .views import *
from django.urls import path


urlpatterns = [
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('profile/', UserView.as_view(), name='user-profile'),
    path("get_csrf_token/", get_csrf_token),
]
