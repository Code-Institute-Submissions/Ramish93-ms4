from django.contrib import admin

from order.models import Order, Testimonial


class OrderAdmin(admin.ModelAdmin):
    list_display = ('subject', 'price', 'status', 'is_active', 'created_at', )
    list_filter = ('is_active', 'status', )
    ordering = ('is_active', '-id',)
    search_fields = ('subject', )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('review', 'rating', 'show_on_homepage', 'is_approved', 'created_at', )
    list_filter = ('is_approved', 'rating', )
    ordering = ('-id',)
    search_fields = ('review', )


admin.site.register(Order, OrderAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
