from django.urls import path
from accounts_module import views
from accounts_module import api

app_name = 'accounts'

urlpatterns = [
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('forget-password/done/', views.ForgetPasswordDoneView.as_view(), name='forget_password_done'),
    path('reset-password/<token>/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('reset/done/', views.ResetPasswordDoneView.as_view(), name='reset_password_done'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change_password'),
    path('profile/<pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('api/change-password/<int:pk>/', api.ChangePasswordView.as_view(), name='api_change_password'),
    path('api/profile/<pk>/', api.UserProfileView.as_view(), name='api_user_profile'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]

