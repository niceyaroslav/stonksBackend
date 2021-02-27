from rest_framework import serializers

from api.models import Transaction, Asset


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ["user"]


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = "__all__"
