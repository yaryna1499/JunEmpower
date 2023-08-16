from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from .models import CustomUser
from .serializer import CustomUserSerializer



def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})


class UserApiView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
