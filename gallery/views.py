from django.views.generic import ListView, DetailView

from gallery.models import GalleryItem


class GalleryItemListView(ListView):
    queryset = GalleryItem.objects.filter(is_active=True).order_by('-created_at')
    paginate_by = 10


class GalleryItemDetailView(DetailView):
    queryset = GalleryItem.objects.filter(is_active=True)
