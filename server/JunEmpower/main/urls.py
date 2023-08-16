from django.urls import path, include
from rest_framework import routers
from .views import *



urlpatterns = [
    path('sign-in/', SignIn.as_view()),
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserApiUpdate.as_view()),
    path('userdelete/<int:pk>/', UserApiDestroy.as_view()),
]