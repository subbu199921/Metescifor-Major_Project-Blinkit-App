from django.urls import path
from . import views
from .views import user_home
from . import payment

urlpatterns = [
    path('', views.product_list, name='home'),
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('vendor/details/', views.vendor_details, name='vendor_details'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('user-home/', user_home, name='user_home'),
    path('order/<int:order_id>/payment/', payment.payment_view, name='payment'),
    path('order/<int:order_id>/payment/verification/', views.payment_verification, name='payment_verification'),
    path('payment/success/', views.payment_success, name='payment_success'),
]