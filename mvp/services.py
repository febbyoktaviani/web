from dateutil.relativedelta import relativedelta
from django.db.models import Avg
from .models import Currency
from .models import CurrencyExchange
from .models import CurrencyExchangeRateHistory


class CurrencyExchangeRateHistoryService():
    def add(self, data):
        source_currency = Currency.objects.get_or_none(pk=data.pop('source_currency'))
        target_currency = Currency.objects.get_or_none(pk=data.pop('target_currency'))
        currency_exchange = CurrencyExchange.objects.filter(
            source_currency=source_currency,
            target_currency=target_currency).first()
        if not currency_exchange:
            raise Exception('currency exchange is not in the list')
        
        data['currency_exchange'] = currency_exchange
        exchange_rate = CurrencyExchangeRateHistory(**data)
        data_added = exchange_rate.save()

    def get_seven_days_average(self, currency_exchange, date):
        seven_days_ago = date - relativedelta(days=7)
        rate_list = CurrencyExchangeRateHistory.objects.filter(
            currency_exchange=currency_exchange, date__range=(seven_days_ago, date))

        if rate_list.count() == 7:
            average_dict = rate_list.aggregate(seven_days_rate=Avg('rate'))
            return average_dict['seven_days_rate']

        return 'insuficient data'


    def get_list_by_date(self, date):
        queryset = CurrencyExchangeRateHistory.objects.filter(date=date)
        exchange_rate_track_list = []
        
        for rate in queryset:
            data = {}
            data['source_currency'] = rate.currency_exchange.source_currency.name
            data['target_currency'] = rate.currency_exchange.target_currency.name
            data['date'] = rate.date.__str__()
            data['rate'] = rate.rate
            data['seven_days_average'] = self.get_seven_days_average(rate.currency_exchange, date)
            exchange_rate_track_list.append(data)

        return exchange_rate_track_list