
from django.contrib import admin
from django.urls import path

from home_module import views
app_name = 'home'
urlpatterns = [path('', views.Home.as_view(),  name='home')]


