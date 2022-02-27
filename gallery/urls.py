from django.urls import path

from gallery.views import GalleryItemListView, GalleryItemDetailView

urlpatterns = [
    path('', GalleryItemListView.as_view(), name='gallery_item_list'),
    path('<int:pk>', GalleryItemDetailView.as_view(), name='gallery_item_detail'),
]
