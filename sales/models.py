from django.db import models
from clients.models import Client
from fertilizers.models import Fertilizer


class Sale(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, blank=True, null=True)
    client_name = models.CharField(max_length=50, blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    fertilizer = models.CharField(max_length=50, blank=True)
    area = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    total_sum = models.IntegerField(blank=True, null=True)
    sale_qty = models.CharField(max_length=30, blank=True)
    group_type = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.fertilizer)


# class SaleItem(models.Model):
#     fertilizer = models.ForeignKey(
#         Fertilizer, on_delete=models.SET_NULL, blank=True, null=True)
#     sale = models.ForeignKey(
#         Sale, on_delete=models.SET_NULL, blank=True, null=True)
#     fertilizer_qty = models.DecimalField(default=0,
#                                          max_digits=10, decimal_places=2, blank=True)

#     def __str__(self):
#         return self.fertilizer
