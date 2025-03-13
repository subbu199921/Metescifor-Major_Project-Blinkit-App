from django.contrib import admin
from .models import Vendor,Category, Product, Customer, Cart, CartItem, Order, OrderItem

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)