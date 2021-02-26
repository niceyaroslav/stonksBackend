from django.contrib import admin

from api.models import Transactions


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass
