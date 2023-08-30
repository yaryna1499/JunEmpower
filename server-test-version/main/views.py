from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import get_token
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from django.contrib.auth import authenticate, login
from .serializers import UserRegisterSerializer, UserLoginSerializer, CustomUserSerializer
from .models import CustomUser
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomSetPagination


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})


class LoginView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        return Response()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serialized_data_user = CustomUserSerializer(user).data
            print(serialized_data_user)
            return Response({'message': 'Авторизация успешна', 'user': serialized_data_user}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Неправильные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)


class UserApiView(generics.ListCreateAPIView):
    pagination_class = CustomSetPagination
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated,)  # не розумію для чого тут IsAuthenticatedOrReadOnly. це означає що читати юзерів може хто завгодно, а створити тільки залогінений, але ти нижче фунцією відміняєшь обмеження на ПОСТ.
    """                                                  # мабудь ти хотіла обмежети перегляд юзерів для незалогінених.. ТОді підійде IsAuthenticated  і твоя логіка запрацює
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


# class UserView(APIView):     Цей вью не потрібен, він дуюдює функціонал наступного
#     permission_classes = (permissions.IsAuthenticated,)  # тут тоді теж саме, міняю на IsAuthenticated
#
#     @swagger_auto_schema(
#         operation_summary="Отримати інформацію про користувача за його ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'user_id',
#                 openapi.IN_PATH,
#                 type=openapi.TYPE_INTEGER,
#                 description='ID користувача',
#                 required=True,
#             ),
#         ],
#         responses={200: CustomUserSerializer(), 400: 'Некоректний ID', 404: 'Користувач не знайдений'},
#     )
#     def get(self, request, user_id):               # user_id треба передавати з урл
#
#         try:
#             user = CustomUser.objects.get(id=user_id)
#         except CustomUser.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = CustomUserSerializer(user)
#         return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)   # тут не можна IsAuthenticated, то зможе кожен залогінений юзер змінити іншого користувача додав кастомний пермісіонс, який перевіряє що цей об'єкт який змінюється дорівнює залогіненному юзеру
    """
    Оновлення користувача(редагування профілю).
    ---
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'patch']   # додав гет, щоб можно було дивитись юзера за id, і тут же отримовати csrf


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)  # теж саме
    """
    Видалення користувача.
    ---
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'delete']   # додав гет, щоб можно було тут же отримовати csrf

