from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if username and password:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                try:
                    user = UserModel._default_manager.get(email=username)
                except UserModel.DoesNotExist:
                    user = None
                    UserModel().set_password(password)

            if user and user.check_password(password) and self.user_can_authenticate(user):
                return user

        return None
