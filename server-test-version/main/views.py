
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import permissions
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsOwnerProjectOrReadOnly
from .pagination import CustomSetPagination



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

    def create(self, request, *args, **kwargs):
        #переопределяємо статус з 400 на  409
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except serializers.ValidationError as e:
            error_data = e.detail
            return Response(error_data, status=status.HTTP_409_CONFLICT)


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
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


class SpecializationApiView(generics.ListAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    """
    Готовий список спеціальностей.
    """
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


#_____________________________project's_view_____________________________________#


class TechnologyApiView(generics.ListCreateAPIView):
    pagination_class = None
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProjectApiView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomSetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsOwnerProjectOrReadOnly, )   #перевірити
    http_method_names = ['get', 'patch']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectDeleteApiView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerProjectOrReadOnly, ) #перевірити


class ImageApiView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ProjectImage.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ImageDeleteApiView(generics.DestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ProjectImage.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)
