from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import get_token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserRegisterSerializer, UserLoginSerializer, CustomUserSerializer
from .models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})


class UserApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Список користувачів(user_list) та створення нового користувача(user_create).
    ---
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_serializer_class(self):
        """
        Визначення класу серіалайзера в залежності від методу запиту.
        """
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Викликаємо метод get_serializer_class() для вибору серіалайзера.
        """
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)
    
    def get_permissions(self):
        """
        Визначення класів дозволів в залежності від методу запиту.
        """
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return super().get_permissions()



class UserView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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
    )
    def get(self, request, user_id):
 
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)



class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    """
    Оновлення користувача(редагування профілю).
    ---
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['put']


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    """
    Видалення користувача.
    ---
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['delete']

