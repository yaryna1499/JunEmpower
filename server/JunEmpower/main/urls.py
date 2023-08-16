from .views import *
from django.urls import path


urlpatterns = [
    path("user/", UserApiView.as_view()),
    path("user/<int:pk>/", UserApiUpdate.as_view()),
    path("userdelete/<int:pk>/", UserApiDestroy.as_view()),
    path("get_csrf_token/", get_csrf_token),
]
