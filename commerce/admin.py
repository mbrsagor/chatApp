from django.contrib import admin
from commerce.models.category import Category, Tag
from commerce.models.product import Product

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
