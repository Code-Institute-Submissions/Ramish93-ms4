from django.views.generic import ListView, DetailView

from order.models import Order


class OrderListView(ListView):
    queryset = Order.objects.filter(is_active=True).order_by('-created_at')
    paginate_by = 10


class OrderDetailView(DetailView):
    queryset = Order.objects.filter(is_active=True)
