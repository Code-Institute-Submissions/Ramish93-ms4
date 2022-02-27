from django.views.generic import TemplateView

from gallery.models import GalleryItem
from order.models import Testimonial, Order


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['orders'] = Order.objects.filter(is_active=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(show_on_homepage=True, is_approved=True)[:2]
        context['gallery_item'] = GalleryItem.objects.filter(is_active=True)[:5]

        return context
