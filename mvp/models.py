from __future__ import unicode_literals

from datetime import timedelta
from dateutil.relativedelta import relativedelta

from django.core import exceptions
from django.db import connection
from django.db import models
from django.db.models import Sum
from django.utils import timezone


class TimeStampedModel(models.Model):

    class Meta(object):
        abstract = True

    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)


class GetInstanceMixin(object):
    def get_or_none(self, **kwargs):
        """Extends get to return None if no object is found based on query."""
        try:
            logger.debug(
                "Getting instance for %s with %s" % (self.model, kwargs))
            instance = self.get(**kwargs)
            logger.info(
                "Got instance primary_key=%s for %s" % (instance.pk, self.model))
            return instance
        except exceptions.ObjectDoesNotExist:
            logger.warn(
                "No instance found for %s with %s" % (self.model, kwargs))
            return None


class CurrencyManager(GetInstanceMixin, models.Manager):
    pass


class Currency(TimeStampedModel):
    name = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=50)

    objects = CurrencyManager()

    class Meta:
        db_table = 'currency'


class CurrencyExchangeManager(GetInstanceMixin, models.Manager):
    pass



class CurrencyExchange(TimeStampedModel):
    source_currency = models.ForeignKey('Currency',
                                       on_delete=models.CASCADE,
                                       related_name='source_currency')
    target_currency = models.ForeignKey('Currency',
                                        on_delete=models.CASCADE,
                                        related_name='target_currency')
    objects = CurrencyExchangeManager()

    class Meta:
        db_table = 'currency_exchange'
        unique_together = ('source_currency', 'target_currency')


class CurrencyExchangeRateHistoryManager(GetInstanceMixin, models.Manager):
    pass


class CurrencyExchangeRateHistory(TimeStampedModel):
    currency_exchange = models.ForeignKey('CurrencyExchange',
                                          on_delete=models.CASCADE,
                                          db_column='currency_exchange_id')
    date = models.DateField()
    rate = models.FloatField()

    objects = CurrencyExchangeRateHistoryManager()

    class Meta:
        db_table = 'currency_exchange_rate_history'
        unique_together = ('date', 'currency_exchange')
            