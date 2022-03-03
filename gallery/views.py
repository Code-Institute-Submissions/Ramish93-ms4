import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from gallery.models import GalleryItem, Cart


class GalleryItemListView(ListView):
    queryset = GalleryItem.objects.filter(is_active=True).order_by('-created_at')
    paginate_by = 10


class GalleryItemDetailView(DetailView):
    queryset = GalleryItem.objects.filter(is_active=True)


class CartDetailView(DetailView):
    def get_object(self, queryset=None):
        cart, created = Cart.objects.get_or_create(user_id=self.request.user.id)
        return cart


class AddRemoveToCartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user_id=self.request.user.id)
        gallery_item = GalleryItem.objects.get(pk=request.GET['id'])
        action = request.GET['action']

        if action == 'add':
            cart.gallery_items.add(gallery_item)
            msg = '{} has been added in cart.'
        else:
            cart.gallery_items.remove(gallery_item)
            msg = '{} has been removed from cart.'

        return JsonResponse({'message': msg.format(gallery_item.title)})


class CheckoutConfigView(View):
    def get(self, request):
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class CreateCheckoutSessionView(View):
    domain_url = settings.STRIPE_REDIRECT_URL
    stripe.api_key = settings.STRIPE_SECRET_KEY

    def get(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=self.domain_url + 'gallery/cart/payment_success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=self.domain_url + 'gallery/cart/payment_cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Logos',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class PaymentSuccessTemplateView(TemplateView):
    template_name = 'gallery/payment_successful.html'


class PaymentCancelledTemplateView(TemplateView):
    template_name = 'gallery/payment_cancelled.html'
