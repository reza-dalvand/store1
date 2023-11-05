from accounts_module.models import CustomUser
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if CustomUser.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value
    #
    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if CustomUser.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError({"username": "This username is already in use."})
    #     return value
    #
    # def update(self, instance, validated_data):
    #     instance.username = validated_data['username']
    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.phone_number = validated_data['phone_number']
    #     instance.email = validated_data['email']
    #
    #     instance.save()
    #
    #     return instance


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
                {'password2': _('passwords not match'), })
        elif len(password) < 4:
            raise serializers.ValidationError(
                {'password2': _('password must be at least 4 characters')})
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
