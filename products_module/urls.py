from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import ProductApi
from .views import ProductsListView, ProductsDetailView, CreateCommentView

app_name = 'products'

router = DefaultRouter()
router.register('api/product', ProductApi, basename='product_api')

urlpatterns = [path('', ProductsListView.as_view(), name='products_list'),
               path('detail/<pk>/', ProductsDetailView.as_view(), name='product_detail'),
               path('create-comment', CreateCommentView.as_view(), name='create_comment')] + router.urls
