from rest_framework.routers import DefaultRouter

from .views import *
from django.urls import path, include


urlpatterns = [
    path("user/", UserApiView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserApiUpdate.as_view(), name="user-profile-edit"),
    path("user_delete/<int:pk>/", UserApiDestroy.as_view(), name="user-profile-delete"),
    path(
        "project/<int:project_id>/comments/",
        ProjectCommentsView.as_view(),
        name="project-comments-list",
    ),
    path(
        "project/<int:project_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="comment-detail",
    ),
    path("project/", ProjectApiView.as_view()),
    path("project/<int:pk>/", ProjectUpdateApiView.as_view()),
    path("project_delete/<int:pk>/", ProjectDeleteApiView.as_view()),
    path("project_image/", ImageApiView.as_view()),
    path("project_image_delete/<int:pk>/", ImageDeleteApiView.as_view()),
    path(
        "user_specialization/",
        SpecializationApiView.as_view(),
        name="user-specialization",
    ),
    path("technologies/", TechnologyApiView.as_view(), name="technologies"),
    path("search/", ProjectApiView.as_view(), name="search"),
    path(
        "likes/",
        LikeViewSet.as_view({"post": "create", "delete": "destroy"}),
        name="likes",
    ),
    path("comments/<int:comment_id>/", CommentDetailView.as_view()),
]
