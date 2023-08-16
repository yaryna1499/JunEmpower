from django.urls import path, include
from rest_framework import routers

from .views import SignIn, UserApiView, UserApiUpdate, UserApiDestroy
                    # UserApiViewSet)
                    # sign_in)
                    # sign_out

# router = routers.DefaultRouter()
# router.register(r'user', UserApiViewSet)


urlpatterns = [
    # path("", main),
    # path("sign-up/", register, name="sign-up"),
    # path("sign-in/", sign_in, name="sign-in"),
    # path("sign-out/", sign_out, name="sign-out"),
    # path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path('sign-in/', SignIn.as_view(), name='sign_in'),
    # path('', include(router.urls))
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserApiUpdate.as_view()),
    path('userdelete/<int:pk>/', UserApiDestroy.as_view()),

    # path('user/<int:pk>/', UserSingleApiView.as_view()),


]