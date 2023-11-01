from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import ProductsListApi
from .views import ProductsListView, ProductsDetailView

app_name = 'products'

router = DefaultRouter()
router.register('api', ProductsListApi, basename='products_api')

urlpatterns = [path('', ProductsListView.as_view(), name='products_list')] + router.urls
