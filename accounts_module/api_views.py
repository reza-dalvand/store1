from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts_module.serializers import RegisterUserSerializer


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
