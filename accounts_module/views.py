import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
from accounts_module.serializers import RegisterUserSerializer
from django.utils.translation import gettext_lazy as _


# Create your views here.


class RegisterAPIView(generics.GenericAPIView):
    """Registers user"""
    serializer_class = RegisterUserSerializer

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        return render(request, './accounts/signup.html', {})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            '''set error for each field in template '''
            field_errors = {}
            for field_name, field_error in serializer.errors.items():
                field_errors[field_name] = field_error[0]
            return render(request, './accounts/signup.html',
                          {"field_errors": field_errors})

        serializer.save()
        return HttpResponseRedirect(reverse('accounts:login'))


class LoginAPIView(APIView):
    """login user"""

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        return render(request, './accounts/signin.html', {})

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email or password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home:home'))
            return render(request, './accounts/signin.html', {'error': _('user not found')})
        return render(request, './accounts/signin.html', {'error': _('fields not be empty')})


class LogoutAPIView(LoginRequiredMixin, APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
