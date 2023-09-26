
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, get_list_or_404
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
from .my_tools import validate_str_to_bool


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
        if self.request.method == "POST":
            return UserRegisterSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Викликаємо метод get_serializer_class() для вибору серіалайзера.
        """
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)

    def get_permissions(self):
        """
        Визначення класів дозволів в залежності від методу запиту.
        """
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        # переопределяємо статус з 400 на  409
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except serializers.ValidationError as e:
            error_data = e.detail
            return Response(error_data, status=status.HTTP_409_CONFLICT)


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticated,
    )
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    """
    Оновлення користувача(редагування профілю).
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "patch"]


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticated,
    )
    """
    Видалення користувача.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "delete"]


class SpecializationApiView(generics.ListAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    """
    Готовий список спеціальностей.
    """
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


# _____________________________project's_view_____________________________________#


class TechnologyApiView(generics.ListCreateAPIView):
    pagination_class = None
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProjectApiView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created')
    serializer_class = ProjectSerializer
    pagination_class = CustomSetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter technologies
        technologies_args = self.request.GET.get('technologies')
        if technologies_args:
            technologies_list = technologies_args.split(',')
            tech_objects = get_list_or_404(Technology, slug__in=technologies_list)
            queryset = queryset.annotate(tech_count=Count('technology',
                                                          filter=Q(technology__in=tech_objects)
                                                          ))
            queryset = queryset.filter(tech_count=len(tech_objects))
        # filter link_hub
        link_hub = validate_str_to_bool(self.request.GET.get('link-hub'))
        if link_hub:
            queryset = queryset.filter(link_hub__isnull=False)
        # filter link_deploy
        link_deploy = validate_str_to_bool(self.request.GET.get('link-deploy'))
        if link_deploy:
            queryset = queryset.filter(link_deploy__isnull=False)

        # # filter in_development
        # in_dev = validate_str_to_bool(self.request.GET.get('in-dev'))
        # if in_dev:
        #     queryset = queryset.filter(in_development=True)
        # # filter is_compiled
        # is_completed = validate_str_to_bool(self.request.GET.get('is-completed'))
        # if is_completed:
        #     queryset = queryset.filter(is_completed=True)

        # filter status
        status_proj = self.request.GET.get('status')
        if status_proj:
            queryset = queryset.filter(status=status_proj)
        # sort
        sort = self.request.GET.get('sort')
        if sort:
            if 'likes' in sort:
                queryset = queryset.annotate(likes_count=Count('likes')).order_by(sort + '_count')
            if 'created' in sort:
                queryset = queryset.order_by(sort)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectCreateSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsOwnerProjectOrReadOnly,)  # перевірити
    http_method_names = ["get", "patch"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectDeleteApiView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerProjectOrReadOnly,)  # перевірити


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
=======
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, get_list_or_404
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
from .my_tools import validate_str_to_bool


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
        if self.request.method == "POST":
            return UserRegisterSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Викликаємо метод get_serializer_class() для вибору серіалайзера.
        """
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)

    def get_permissions(self):
        """
        Визначення класів дозволів в залежності від методу запиту.
        """
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        # переопределяємо статус з 400 на  409
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except serializers.ValidationError as e:
            error_data = e.detail
            return Response(error_data, status=status.HTTP_409_CONFLICT)


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticated,
    )
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    """
    Оновлення користувача(редагування профілю).
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "patch"]


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticated,
    )
    """
    Видалення користувача.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "delete"]


class SpecializationApiView(generics.ListAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    """
    Готовий список спеціальностей.
    """
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


# _____________________________project's_view_____________________________________#


class TechnologyApiView(generics.ListCreateAPIView):
    pagination_class = None
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProjectApiView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("-created")
    serializer_class = ProjectSerializer
    pagination_class = CustomSetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter technologies
        technologies_args = self.request.GET.get("technologies")
        if technologies_args:
            technologies_list = technologies_args.split(",")
            tech_objects = get_list_or_404(Technology, slug__in=technologies_list)
            queryset = queryset.annotate(
                tech_count=Count("technology", filter=Q(technology__in=tech_objects))
            )
            queryset = queryset.filter(tech_count=len(tech_objects))
        # filter link_hub
        link_hub = validate_str_to_bool(self.request.GET.get("link-hub"))
        if link_hub:
            queryset = queryset.filter(link_hub__isnull=False)
        # filter link_deploy
        link_deploy = validate_str_to_bool(self.request.GET.get("link-deploy"))
        if link_deploy:
            queryset = queryset.filter(link_deploy__isnull=False)

        # # filter in_development
        # in_dev = validate_str_to_bool(self.request.GET.get('in-dev'))
        # if in_dev:
        #     queryset = queryset.filter(in_development=True)
        # # filter is_compiled
        # is_completed = validate_str_to_bool(self.request.GET.get('is-completed'))
        # if is_completed:
        #     queryset = queryset.filter(is_completed=True)

        # filter status
        status_proj = self.request.GET.get("status")
        if status_proj:
            queryset = queryset.filter(status=status)
        # sort
        sort = self.request.GET.get("sort")
        if sort:
            if "likes" in sort:
                queryset = queryset.annotate(likes_count=Count("likes")).order_by(
                    sort + "_count"
                )
            if "created" in sort:
                queryset = queryset.order_by(sort)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectCreateSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsOwnerProjectOrReadOnly,)  # перевірити
    http_method_names = ["get", "patch"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class ProjectDeleteApiView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerProjectOrReadOnly,)  # перевірити


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

