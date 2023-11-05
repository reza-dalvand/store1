from django.urls import path
from accounts_module import views
from accounts_module import api


app_name = 'accounts'
urlpatterns = [
    path('user-profile/<pk>/', api.UserProfileView.as_view(), name='user_profile'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]

