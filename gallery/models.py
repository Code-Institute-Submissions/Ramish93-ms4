from django.db import models
from django.utils import timezone


class GalleryItem(models.Model):
    STATUSES = (
        ('Available', 'Available'),
        ('Coming-Soon', 'Coming-Soon'),
        ('Out-of-Stock', 'Out-of-Stock')
    )

    title = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=5)
    size = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUSES, null=True, blank=True)
    image = models.ImageField(upload_to='gallery_item/%Y/%m/%d/', default='')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
