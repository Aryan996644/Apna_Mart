from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Allows authentication using either username or email address.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        login_id = username or kwargs.get(UserModel.USERNAME_FIELD) or kwargs.get('email')
        if not login_id or not password:
            return None

        user = UserModel.objects.filter(
            Q(username__iexact=login_id) | Q(email__iexact=login_id)
        ).first()

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
