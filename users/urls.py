from django.urls import path
from .views import RegisterView, LoginView, ReferralView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('referral/<str:referral_code>/', ReferralView.as_view(), name='referral'),
]
