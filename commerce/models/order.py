from django.db import models

from commerce.models import Product
from commerce.models.core import CoreEntity
from commerce.utils.enum import STATUS, PAYMENT


class Order(CoreEntity):
    full_name = models.CharField(max_length=60)
    phn_number = models.CharField(max_length=14)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    payment_status = models.IntegerField(choices=PAYMENT.payment_choices(), default=PAYMENT.CASH_ON_DELIVERY.value)
    status = models.IntegerField(choices=STATUS.order_status(), default=STATUS.PENDING.value)

    def __str__(self):
        return f"Customer Name: {self.full_name} Phone Number: {self.phn_number}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    orders = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.price * self.quantity
