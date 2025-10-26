# urls.py
from django.urls import path
from backend.views import RegisterAccount, LoginAccount, ConfirmAccount, CategoryView, \
    ShopView, BasketView, AccountDetails

urlpatterns = [
    path('auth/register', RegisterAccount.as_view(), name='register'),
    path('auth/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('auth/login', LoginAccount.as_view(), name='login'),
    path('auth/details', AccountDetails.as_view(), name='user-details'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
]