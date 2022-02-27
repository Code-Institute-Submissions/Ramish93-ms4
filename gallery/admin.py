from django.contrib import admin

from gallery.models import GalleryItem


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size', 'status', 'is_active', 'created_at', )
    list_filter = ('is_active', 'status', )
    ordering = ('is_active', '-id',)
    search_fields = ('title', )


admin.site.register(GalleryItem, GalleryItemAdmin)
