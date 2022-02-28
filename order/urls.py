from django.urls import path

from order.views import OrderListView, OrderDetailView, OrderCreateView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('new', OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]
