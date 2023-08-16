
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view as drf_yasg_get_schema_view

from drf_yasg import openapi

schema_view_openapi = drf_yasg_get_schema_view(
    openapi.Info(
        title="API endpoints for JunEmpower",
        default_version='v1',
        description="endpoint to get csrf: GET http://localhost:1443/get_csrf_token/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("main.urls"), name="main"),
    path('redoc/', schema_view_openapi.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

