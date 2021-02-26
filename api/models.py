from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Transactions(models.Model):
    user = models.ForeignKey(User,
                             related_name='transactions',
                             on_delete=models.CASCADE,
                             null=True)
    amount_cash = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    amount_crypto = models.DecimalField(max_digits=50, decimal_places=20, null=True)
    date_of_transfer = models.DateTimeField(null=True)

