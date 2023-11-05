from django.urls import path
from accounts_module import views
from accounts_module import api

app_name = 'accounts'

urlpatterns = [
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='change_password'),
    path('profile/<pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('api/change_password/<int:pk>/', api.ChangePasswordView.as_view(), name='api_change_password'),
    path('api/profile/<pk>/', api.UserProfileView.as_view(), name='api_user_profile'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]

