from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from accounts_module.models import CustomUser

'''This module serializes registration data '''
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {

            'password': {'write_only': True}
        }

    def email_checker(self):
        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'this email already exists'})

    def password_checker(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'passwords did not match'})
        elif len(password) < 4:
            raise serializers.ValidationError(
                {'error': 'passwords length should be at least 4'})

    def prepare_user_account(self):
        self.user_account = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'])
        self.user_account.set_password(self.validated_data['password'])

    def save(self):
        self.email_checker()
        self.password_checker()
        self.prepare_user_account()
        self.user_account.save()
        return self.user_account


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def email_checker(self):
        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'this email already exists'})

    def prepare_user_account(self):
        self.user_account = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'])
        self.user_account.set_password(self.validated_data['password'])

    def save(self):
        self.email_checker()
        self.password_checker()
        self.prepare_user_account()
        self.user_account.save()
        return self.user_account
