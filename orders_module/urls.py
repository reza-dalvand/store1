from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .api import OrderDetailViewSet

app_name = 'order'

router = DefaultRouter()
router.register('api/list', OrderDetailViewSet, basename='order-api')

urlpatterns = [
    # api views
    # path('list/', views.OrderView.as_view(), name='order'),
] + router.urls

