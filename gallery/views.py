from django.views.generic import ListView, DetailView

from gallery.models import GalleryItem, Cart


class GalleryItemListView(ListView):
    queryset = GalleryItem.objects.filter(is_active=True).order_by('-created_at')
    paginate_by = 10


class GalleryItemDetailView(DetailView):
    queryset = GalleryItem.objects.filter(is_active=True)


class CartDetailView(DetailView):
    def get_object(self, queryset=None):
        # return Cart.objects.get(user_id=self.request.user.id)
        return Cart.objects.first()
