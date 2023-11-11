from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders_module.models import Order, OrderDetail
from orders_module.serializers import OrderSerializer, OrderDetailSerializer


class OrderDetailViewSet(ModelViewSet):
    """manage orders of user"""
    serializer_class = OrderSerializer
    queryset = OrderDetail.objects.all()

    def list(self, request, *args, **kwargs):
        basket, created = Order.objects.get_or_create(user_id=self.request.user.id, is_open=True)
        serializer = OrderSerializer(basket)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        basket, created = Order.objects.prefetch_related('orders').get_or_create(user_id=self.request.user.id,
                                                                                 is_open=True)

        serializer = OrderDetailSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            detail = basket.orders.filter(product=request.POST.get('product_id')).first()
            if detail:
                detail.count += int(request.POST.get('count'))
                detail.save()
                return Response(status.HTTP_201_CREATED)
            OrderDetail.objects.create(
                product_id=request.POST.get('product_id'), order_id=basket.id, count=request.POST.get('count'))
            return Response(status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        basket, created = Order.objects.prefetch_related('orders').get_or_create(user_id=self.request.user.id,
                                                                                 is_open=True)
        if kwargs.get('pk'):
            basket.orders.filter(id=kwargs.get('pk')).delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
