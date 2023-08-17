from django.contrib import admin

from core.models import Wallet, Transaction


class TransactionInline(admin.TabularInline):
    model = Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "balance"]
    inlines = [
        TransactionInline,
    ]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "wallet", "txid", "amount"]
