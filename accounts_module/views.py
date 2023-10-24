import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from django.urls import reverse
from accounts_module.serializer import RegisterUserSerializer
from django.utils.translation import gettext_lazy as _


# Create your views here.


class RegisterAPIView(generics.GenericAPIView):
    """Registers user"""
    serializer_class = RegisterUserSerializer

    def get(self, request):
        return render(request, './accounts/signup.html', {})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            '''set error for each field in template '''
            field_errors = {}
            for field_name, field_error in serializer.errors.items():
                field_errors[field_name] = field_error[0]
            # return Response({'Register': 'Bad Request'}, status.HTTP_400_BAD_REQUEST)
            return render(request, './accounts/signup.html',
                          {"field_errors": field_errors})

        serializer.save()
        # return Response(data, status.HTTP_201_CREATED)
        return HttpResponseRedirect(reverse('accounts:login'))


class LoginAPIView(APIView):
    """login user"""

    def get(self, request):
        # return Response({'login': 'Successful'}, status=status.HTTP_200_OK)
        return render(request, './accounts/signin.html', {})

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email or password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # return Response({'login': 'Successful'}, status=status.HTTP_200_OK)
                return HttpResponseRedirect(reverse('home:home'))
            # return Response({'login': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
            return render(request, './accounts/signin.html', {'error': _('کاربری با این مشخصات یافت نشد.')})
        # return Response({'login': 'Bad Request'}, status=status.HTTP_BAD_REQUEST)
        return render(request, './accounts/signin.html', {'error': _('فیلد های مورد نظر را پر کنید')})


class LogoutAPIView(LoginRequiredMixin, APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
