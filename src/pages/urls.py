from django.urls import path

from .views import (
	ItemDetailView,
	CheckoutView,
	home,
	Item_ListView,
	OrderSummaryView,
	add_to_cart,
	remove_from_cart,
	remove_single_item_from_cart,
	PaymentView,
	AddCouponView,
	RequestRefundView
	)

app_name = 'pages'

urlpatterns = [

    path('', home, name='home'),
    path('item_list/', Item_ListView.as_view(), name='item_list'),
    path('products/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'), 
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order_summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')

   ]