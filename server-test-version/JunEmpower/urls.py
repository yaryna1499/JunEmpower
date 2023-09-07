from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view as drf_yasg_get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

schema_view_openapi = drf_yasg_get_schema_view(
    openapi.Info(
        title="API endpoints for JunEmpower",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("admin/", admin.site.urls),
    path("", include("main.urls"), name="main"),

    path("redoc/", schema_view_openapi.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)