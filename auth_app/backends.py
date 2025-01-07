from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    """
    Custom authentication backend to allow login with either username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username provided is an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Fallback to username if email doesn't match
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
