from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    # api views
    path('list/', views.OrderView.as_view(), name='order'),
]

