import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts_module.models import CustomUser
from accounts_module.serializers import RegisterUserSerializer, UserProfileSerializer, ChangePasswordSerializer, \
    ResetPasswordEmailSerializer, ChangeForgetPasswordSerializer


class RegisterAPIView(generics.GenericAPIView):
    """Registers user"""
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'Register': 'Bad Request'}, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    """login user"""

    def get(self, request):
        if request.user.is_authenticated:
            return Response({'login': 'redirect to home'}, status=status.HTTP_302_FOUND)
        return Response({'login': 'Successful'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email or password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return Response({'login': 'Successful'}, status=status.HTTP_200_OK)
            return Response({'login': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'login': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(LoginRequiredMixin, APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'logout': 'Successful'}, status=status.HTTP_200_OK)


class UserProfileView(generics.UpdateAPIView):
    """update user profile"""
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """change password in user profile"""
    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer


class ResetPasswordView(APIView):
    """send reset password email"""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            user = CustomUser.objects.filter(email__iexact=email).first()
            # url = f'http://127.0.0.1:8000/auth/api/change-password/{user.token}'
            # send_mail_to_users(_("change password"), f'click on link {url}', [user.email])
            return Response(status.HTTP_200_OK)


class ChangeForgetPasswordView(APIView):
    """change password"""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ChangeForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user_token = kwargs.get('token')
            new_password = serializer.data.get('new_password')
            confirm_password = serializer.data.get('confirm_password')
            user: CustomUser = CustomUser.objects.filter(token__iexact=user_token).first()
            if user and new_password == confirm_password:
                user.set_password(new_password)
                user.token = uuid.uuid4()
                user.save()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
