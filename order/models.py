from django.db import models
from django.urls import reverse
from django.utils import timezone


class Order(models.Model):
    STATUSES = (
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('Payment Pending', 'Payment Pending'),
        ('Dispatched', 'Dispatched'),
        ('Closed', 'Closed')
    )

    subject = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=3000, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=5)

    status = models.CharField(max_length=30, choices=STATUSES, null=True, blank=True)
    attachment = models.ImageField(upload_to='order_attachment/%Y/%m/%d/', default='')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.subject)

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})


class Testimonial(models.Model):
    RATING_SCORE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    review = models.TextField(max_length=3000, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_SCORE)

    is_approved = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
