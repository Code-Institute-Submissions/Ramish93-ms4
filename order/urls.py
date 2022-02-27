from django.urls import path

from order.views import OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('<int:pk>', OrderDetailView.as_view(), name='Order_detail'),
]
