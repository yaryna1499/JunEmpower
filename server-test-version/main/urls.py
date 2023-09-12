from .views import *
from django.urls import path


urlpatterns = [

    path("user/", UserApiView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserApiUpdate.as_view(), name="user-profile-edit"),
    path("user_delete/<int:pk>/", UserApiDestroy.as_view(), name="user-profile-delete"),
    path('project/', ProjectApiView.as_view()),
    path('project/<int:pk>/', ProjectUpdateApiView.as_view()),
    path('project_delete/<int:pk>/', ProjectDeleteApiView.as_view()),
    path('project_image/', ImageApiView.as_view()),
    path('project_image_delete/<int:pk>/', ImageDeleteApiView.as_view()),
    path("user_specialization/", SpecializationApiView.as_view(), name="user-specialization"),
    path("technology/", TechnologyApiView.as_view(), name="technology"),


]
