from django.urls import path

from signup.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup_view'),
]
