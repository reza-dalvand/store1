from django.urls import path
from accounts_module import views


app_name = 'accounts'
urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('logout', views.LogoutAPIView.as_view(), name='logout'),
]

