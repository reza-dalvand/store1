from django.urls import path

from .api import ProductsListApi
from .views import ProductsListView

app_name = 'products'

urlpatterns = [path('', ProductsListView.as_view(), name='products_list'),
               path('api/', ProductsListApi.as_view(), name='products_list_api')]
