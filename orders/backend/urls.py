# urls.py
from django.urls import path
from backend.views import RegisterAccount, LoginAccount, ConfirmAccount, CategoryView, \
    ShopView, BasketView, AccountDetails, PartnerOrders, PartnerState, PartnerUpdate, OrderView, ProductInfoView, ContactView

urlpatterns = [
    path('auth/register', RegisterAccount.as_view(), name='register'),
    path('auth/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('auth/login', LoginAccount.as_view(), name='login'),
    path('auth/details', AccountDetails.as_view(), name='user-details'),
    path('auth/contact', ContactView.as_view(), name='user-contact'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('partner/orders', PartnerOrders.as_view(), name='partner_orders'),
    path('partner/state', PartnerState.as_view(), name='partner_state'),
    path('partner/update', PartnerUpdate.as_view(), name='partner_update'),
    path('order', OrderView.as_view(), name='order'),
    path('products', ProductInfoView.as_view(), name='shops'),
]