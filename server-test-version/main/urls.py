from .views import *
from django.urls import path, include

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('auth/', include('rest_framework.urls')),
    path("user/", UserApiView.as_view(), name="user-list"),
    # path("profile/<int:user_id>", UserView.as_view(), name="user-profile"),
    path("user/<int:pk>/", UserApiUpdate.as_view(), name="user-profile-edit"),
    path("user_delete/<int:pk>/", UserApiDestroy.as_view(), name="user-profile-delete"),
    path("get_csrf_token/", get_csrf_token),
]
