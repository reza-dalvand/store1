from accounts_module.models import CustomUser
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password2': _('پسورد با تایید پسورد همخوانی ندارد')})
        elif len(password) < 4:
            raise serializers.ValidationError(
                {'password2': _('طول پسورد باید بیشتر از 4 کاراکتر باشد')})
        return data

    def prepare_user_account(self):
        self.user_account = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'])
        self.user_account.set_password(self.validated_data['password'])

    def save(self):
        self.prepare_user_account()
        self.user_account.save()
        return self.user_account
