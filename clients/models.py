from django.db import models
from django.contrib.auth.models import User
from fertilizers.models import Fertilizer


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client_name = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=50, blank=True)
    community = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=50, blank=True)
    potential = models.CharField(max_length=50, blank=True)
    passport_num = models.CharField(max_length=50, blank=True)
    tax_code = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=1000, blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class Monitoring(models.Model):

    CONDITION_CHOICES = [
        ('լավ', 'լավ'),
        ('վատ', 'վատ'),
        ('գերազանց', 'գերազանց')
    ]
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    condition = models.CharField(
        max_length=200, choices=CONDITION_CHOICES, blank=True)
    details = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} մոնիթորինգ"
