from django.db import models


class Fertilizer(models.Model):

    QUANTITY_CHOICES = [
        ('ltr', 'լիտր'),
        ('kg', 'կգ')
    ]

    fertilizer_name = models.CharField(max_length=30, blank=True)

    measurement_unit = models.CharField(
        max_length=50, choices=QUANTITY_CHOICES, blank=True)
    expense_norm = models.DecimalField(
        max_digits=10, decimal_places=1, blank=True)
    price = models.IntegerField()

    @property
    def get_price_norm(self):
        return self.price*self.expense_norm

    def __str__(self):
        return self.fertilizer_name
