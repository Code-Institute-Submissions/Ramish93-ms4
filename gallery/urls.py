from django.urls import path

from gallery.views import (
    GalleryItemListView, GalleryItemDetailView, CartDetailView, CreateCheckoutSessionView, CheckoutConfigView,
    PaymentSuccessTemplateView, PaymentCancelledTemplateView
)

urlpatterns = [
    path('', GalleryItemListView.as_view(), name='gallery_item_list'),
    path('<int:pk>', GalleryItemDetailView.as_view(), name='gallery_item_detail'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cart_detail'),
    path('cart/checkout-config-view', CheckoutConfigView.as_view(), name='checkout_config_view'),
    path('cart/create-checkout-session', CreateCheckoutSessionView.as_view(), name='create_checkout_view'),
    path('cart/payment_success', PaymentSuccessTemplateView.as_view(), name='payment_success_view'),
    path('cart/payment_cancelled', PaymentCancelledTemplateView.as_view(), name='payment_cancelled_view'),
]
