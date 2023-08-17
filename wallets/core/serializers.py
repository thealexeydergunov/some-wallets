from django.db import transaction
from django.db.models import Sum
from rest_framework import serializers

from core.models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
        read_only_fields = ['balance']

    def save(self, **kwargs):
        with transaction.atomic():
            if self.instance:
                self.validated_data['balance'] = Transaction.objects.filter(
                    wallet_id=self.instance.wallet_id).aggregate(Sum('amount')).get('amount__sum') or 0
            else:
                self.validated_data['balance'] = 0
            super().save(**kwargs)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def save(self, **kwargs):
        with transaction.atomic():
            super().save()
            Wallet.objects.filter(id=self.validated_data['wallet'].id).update(balance=Transaction.objects.filter(
                    wallet_id=self.instance.wallet_id).aggregate(Sum('amount')).get('amount__sum') or 0)
