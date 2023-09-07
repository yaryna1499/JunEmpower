from .views import *
from django.urls import path


urlpatterns = [

    path("user/", UserApiView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserApiUpdate.as_view(), name="user-profile-edit"),
    path("user_delete/<int:pk>/", UserApiDestroy.as_view(), name="user-profile-delete"),

]
