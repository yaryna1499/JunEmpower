from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        user = User.objects.filter(Q(email=username)).first()
        if user is None:
            user = User.objects.filter(Q(username=username)).first()

        if user and user.check_password(password):
            return user

        return None
