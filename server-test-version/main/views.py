

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import permissions, viewsets
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsOwnerProjectOrReadOnly
from .pagination import CustomSetPagination
from .filters import *


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
    filter_backends = [CustomSearchFilter,
                       TechnologiesFilter,
                       StatusFilter,
                       LinkDeployFilter,
                       LinkHubFilter,
                       SortFilter]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response(status=status.HTTP_204_NO_CONTENT)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['post', 'delete']

    def create(self, request, *args, **kwargs):
        author = request.user
        request.data['author'] = author.id
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project_id = request.data.get('project')
        try:
            like = Like.objects.get(project=project_id, author=request.user)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'detail': 'Does not exist like '}, status=status.HTTP_404_NOT_FOUND)


#

class ProjectCommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Comment.objects.filter(project=project_id)

    def create(self, request, *args, **kwargs):
        data = request.data

        data['project'] = self.kwargs.get('project_id')
        data['author'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerProjectOrReadOnly]
    http_method_names = ['get', 'patch', 'delete']

    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        return comment

