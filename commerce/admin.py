from django.contrib import admin
from commerce.models.category import Category, Tag, Model
from commerce.models.product import Product
from commerce.models.order import Order, OrderItem

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Model)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
