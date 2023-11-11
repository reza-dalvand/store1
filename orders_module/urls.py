from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .api import OrderDetailViewSet, send_request, verify

app_name = 'order'

router = DefaultRouter()
router.register('api/list', OrderDetailViewSet, basename='order-api')

urlpatterns = [path('list/', views.OrderView.as_view(), name='order'),
               path('api/request/', send_request, name='request'),
               path('api/verify/', verify, name='verify')] + router.urls
