from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Transaction(models.Model):
    user = models.ForeignKey(User,
                             related_name='transactions',
                             on_delete=models.CASCADE,
                             null=True)
    asset = models.CharField(max_length=20, null=True)
    currency = models.CharField(max_length=3, null=True)
    amount_cash = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    amount_crypto = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True)
    date_of_transfer = models.DateTimeField(null=True)


class Asset(models.Model):
    user = models.ForeignKey(User,
                             related_name='assets',
                             on_delete=models.CASCADE,
                             null=True)
    asset = models.CharField(max_length=20, null=True)
    total_investment = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    current_asset_value = models.DecimalField(max_digits=50, decimal_places=2, null=True)
