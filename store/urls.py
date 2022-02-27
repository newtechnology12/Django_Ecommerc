from django.urls import path

from store import views as store_views
from qr_code import views as qrcode_views

urlpatterns = [
	#Leave as empty string for base url
	path('qrcode/', qrcode_views.home_view, name='home_views'),
	path('', store_views.store, name="store"),
	path('cart/', store_views.cart, name="cart"),
	path('checkout/', store_views.checkout, name="checkout"),
	path('update_item/', store_views.updateItem, name="update_item"),
	path('process_order/', store_views.processOrder, name="process_order"),

]