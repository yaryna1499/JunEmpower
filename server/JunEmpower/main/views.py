import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import CustomUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class SignIn(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            serializer_user = CustomUserSerializer(user)
            return Response(serializer_user.data)
        return JsonResponse({'message': 'Unsuccessfully!'})


class UserApiView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = (IsAdminOrReadOnly, )


