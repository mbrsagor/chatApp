from django.db import models
from django.contrib.auth.models import User

from commerce.models import Product
from commerce.models.core import CoreEntity
from commerce.utils.enum import STATUS, PAYMENT


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.id

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discounted_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discounted_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discounted_item_price()
        return self.get_total_item_price()


class Order(CoreEntity):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderCustomer')
    ref_code = models.CharField(max_length=20, default="0")
    items = models.ManyToManyField(OrderItem, related_name='orders')
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=150, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS.order_status(), default=STATUS.PENDING.value)
    payment = models.IntegerField(choices=PAYMENT.payment_choices(), default=PAYMENT.CASH_ON_DELIVERY.value)

    def __str__(self):
        return self.customer.username
