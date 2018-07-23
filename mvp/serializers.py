from rest_framework import serializers


from .models import Currency
from .models import CurrencyExchange
from .models import CurrencyExchangeRateHistory


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name')


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    source_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)

    class Meta:
        model = CurrencyExchange
        fields = ('id', 'source_currency', 'target_currency')


class CurrencyExchangeCreateSerializer(serializers.Serializer):
    source_currency = serializers.IntegerField()
    target_currency = serializers.IntegerField()


class CurrencyExchangeRateHistoryCreateSerializer(serializers.Serializer):
    source_currency = serializers.IntegerField(required=True)
    target_currency = serializers.IntegerField(required=True)
    rate = serializers.FloatField(required=True)
    date = serializers.DateField(required=True)
