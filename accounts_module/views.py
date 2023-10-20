from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from accounts_module.serializer import RegisterUserSerializer


# Create your views here.


class RegisterAPIView(generics.GenericAPIView):
    """Registers user"""
    serializer_class = RegisterUserSerializer

    def get(self, request):
        return render(request, './accounts/signin_signup.html', {})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            user_account = serializer.save()
            data['response'] = "Registration Successful!"
            token = Token.objects.get(user=user_account).key
            data['token'] = token

        Response(data, status.HTTP_201_CREATED)
        return HttpResponseRedirect(reverse('home:home'))


class LoginAPIView(APIView):
    """login user"""

    def get(self, request):
        return render(request, './accounts/signin_signup.html', {})

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")
        password = request.data.get("password")
        print(email, password, 'password')
        if email is None or password is None:

            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        Response({'token': token.key},
                 status=status.HTTP_200_OK)
        return HttpResponseRedirect(reverse('home:home'))


class LogoutAPIView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        """Deletes authentication token"""
        request.user.auth_token.delete()
        return Response({'success': 'Logged out successfully'},
                        status=status.HTTP_200_OK)
