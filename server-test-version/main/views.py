
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserRegisterSerializer, CustomUserSerializer, MyTokenObtainPairSerializer
from .models import CustomUser
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomSetPagination
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserApiView(generics.ListCreateAPIView):
    pagination_class = CustomSetPagination
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated,)  
    """
    Список користувачів(user_list) та створення нового користувача(user_create).
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



class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    """
    Оновлення користувача(редагування профілю).
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'patch']


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    """
    Видалення користувача.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'delete']

