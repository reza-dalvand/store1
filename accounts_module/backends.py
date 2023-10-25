from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class RegisterWithEmail(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        """email contain of username or email address"""
        try:
            user = UserModel.objects.get(Q(username__iexact=email) | Q(email__iexact=email))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=email) | Q(email__iexact=email)).order_by(
                'id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
