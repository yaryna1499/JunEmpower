from .views import *
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API endpoints for JunEmpower",
        default_version='v1',
        description="endpoint to get csrf: GET http://localhost:1443/get_csrf_token/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("user/", UserApiView.as_view()),
    path("user/<int:pk>/", UserApiUpdate.as_view()),
    path("userdelete/<int:pk>/", UserApiDestroy.as_view()),
    path("get_csrf_token/", CsrfTokenView.as_view()),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
