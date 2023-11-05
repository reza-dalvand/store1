import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

from accounts_module.models import CustomUser
from accounts_module.serializers import RegisterUserSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny


class RegisterAPIView(generics.GenericAPIView):
    """Registers user, validate form data with serializer instead of model form"""
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        return render(request, 'accounts/signup.html', {})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            '''set error for each field in template '''
            field_errors = {}
            for field_name, field_error in serializer.errors.items():
                field_errors[field_name] = field_error[0]
            # return Response({'Register': 'Bad request'}, status.HTTP_400_BAD_REQUEST)
            return render(request, 'accounts/signup.html', {"field_errors": field_errors})

        serializer.save()
        # return Response({'Register': 'successfully'}, status.HTTP_201_CREATED)
        return HttpResponseRedirect(reverse('accounts:login'))


class LoginAPIView(APIView):
    """login user"""
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        return render(request, 'accounts/signin.html', {})

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email or password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # return Response({'login': 'ok'}, status.HTTP_200_OK)
                return HttpResponseRedirect(reverse('home:home'))
            # return Response({'login': 'User Not Found'}, status.HTTP_404_NOT_FOUND)
            return render(request, 'accounts/signin.html', {'error': _('user not found')})
        # return Response({'login': 'Bad request'}, status.HTTP_400_BAD_REQUEST)
        return render(request, 'accounts/signin.html', {'error': _('fields not be empty')})


class LogoutAPIView(LoginRequiredMixin, APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    context_object_name = 'user'
    fields = ["username", 'email', 'first_name', 'last_name', 'phone_number']
    template_name = 'accounts/profile.html'

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.filter(id=user_id).first()
        if user and request.user.id == user.id:
            user.first_name = request.POST.get('first-name')
            user.last_name = request.POST.get('last-name')
            user.email = request.POST.get('email')
            user.username = request.POST.get('username')
            user.phone_number = request.POST.get('phone-number')
            user.save()
            return redirect(reverse('accounts:user_profile', args=[user_id]))
        return redirect(reverse('accounts:user_profile', args=[user_id]))


class ChangePasswordView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    context_object_name = 'user'
    fields = ['password']
    template_name = 'accounts/profile.html'

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.filter(id=user_id).first()
        old_password = request.POST.get('old')
        new_password = request.POST.get('new')
        confirm_password = request.POST.get('confirm')
        if user and request.user.id == user.id:
            print(user.check_password(old_password), 'Password changed')
            if user.check_password(old_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return logout(request)
        return redirect(reverse('accounts:change_password', args=[user_id]))
