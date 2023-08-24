from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import get_token
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserRegisterSerializer, UserLoginSerializer, CustomUserSerializer
from .models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_summary="Зареєструвати нового користувача",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Ім\'я користувача'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email користувача'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль користувача'),
            },
            required=['username', 'email', 'password'],
        ),
        responses={201: UserRegisterSerializer(), 400: 'Некоректні дані'},
        tags=['User'],
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=data['email'], password=data['password'])

            if user is not None:
                login(request, user)
                return Response({'message': 'Логін успішний', 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Користувача не знайдено'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @swagger_auto_schema(
        operation_summary="Вилогінитись",
        manual_parameters=[
            openapi.Parameter(
                'user_id',
                openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID користувача',
                required=True,
            ),
        ],
        responses={200: "HTTP_200_OK"},
        tags=['User'],
    )
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)




class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_summary="Отримати інформацію про користувача за його ID",
        manual_parameters=[
            openapi.Parameter(
                'user_id',
                openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID користувача',
                required=True,
            ),
        ],
        responses={200: CustomUserSerializer(), 400: 'Некоректний ID', 404: 'Користувач не знайдений'},
        tags=['User'],
    )
    def get(self, request, user_id):
        """
        Отримати інформацію про користувача за його ID.
        """
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
