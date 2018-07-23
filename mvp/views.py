from datetime import datetime

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .constants import ErrorTemplateMessage
from .models import Currency
from .models import CurrencyExchange
from .serializers import CurrencySerializer
from .serializers import CurrencyExchangeSerializer
from .serializers import CurrencyExchangeCreateSerializer
from .serializers import CurrencyExchangeRateHistoryCreateSerializer
from .services import CurrencyExchangeRateHistoryService


class CurrencyListView(generics.ListAPIView):
    """
    endpoint to retrieve listed currency
    """
    permission_classes = (AllowAny, )
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.all()


class CurrencyExchangeListCreateView(generics.ListCreateAPIView):
    """
     endpoint to retrieve, add, delete currency exchange
    """
    permission_classes = (AllowAny, )
    serializer_class = CurrencyExchangeSerializer


    def get_queryset(self):
        return CurrencyExchange.objects.all()


    def post(self, request, *args, **kwargs):
        data = request.data

        if not 'source_currency' in data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data=ErrorTemplateMessage(('source_currency')).missing_required())
        if not 'target_currency' in data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data=ErrorTemplateMessage(('target_currency')).missing_required())

        serializer = CurrencyExchangeCreateSerializer(data=data)
        if serializer.is_valid():
            source_currency = Currency.objects.get_or_none(pk=serializer.data['source_currency'])
            if not source_currency:
                return Response(status=HTTP_400_BAD_REQUEST,
                                data=ErrorTemplateMessage(('currency')).not_found())
            target_currency = Currency.objects.get_or_none(pk=serializer.data['target_currency'])
            if not target_currency:
                return Response(status=HTTP_400_BAD_REQUEST,
                                data=ErrorTemplateMessage(('currency')).not_found())

            CurrencyExchange.objects.create(source_currency=source_currency,
                                            target_currency=target_currency)

        return Response(status=HTTP_201_CREATED, data='success add currency exchange to track')


    def delete(self, request, *args, **kwargs):
        data = request.data

        if not 'source_currency' in data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data=ErrorTemplateMessage(('source_currency')).missing_required())
        if not 'target_currency' in data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data=ErrorTemplateMessage(('target_currency')).missing_required())

        serializer = CurrencyExchangeCreateSerializer(data=data)
        if serializer.is_valid():
            source_currency = Currency.objects.get_or_none(pk=serializer.data['source_currency'])
            if not source_currency:
                return Response(status=HTTP_400_BAD_REQUEST,
                                data=ErrorTemplateMessage(('currency')).not_found())
            target_currency = Currency.objects.get_or_none(pk=serializer.data['target_currency'])
            if not target_currency:
                return Response(status=HTTP_400_BAD_REQUEST,
                                data=ErrorTemplateMessage(('currency')).not_found())

            currency_exchange = CurrencyExchange.objects.filter(
                source_currency=source_currency, target_currency=target_currency).first()

            if not currency_exchange:
                return Response(status=HTTP_404_NOT_FOUND,
                                data=ErrorTemplateMessage(('currency_exchange')).not_found())

            currency_exchange.delete()
            return Response(status=HTTP_202_ACCEPTED,
                            data='success remove currency exchange from track')
          


class CurrencyExchangeRateHistoryListView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        date = request.query_params.get('date', None)
        if date is None:
            return Response(status=HTTP_400_BAD_REQUEST)

        date = datetime.strptime(date, '%Y-%m-%d').date()
        exchange_track_list = CurrencyExchangeRateHistoryService().get_list_by_date(date)

        return Response(status=HTTP_200_OK, data=exchange_track_list)

    def post(self, request):
        data = request.data
        serializer = CurrencyExchangeRateHistoryCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.data
            print(validated_data)
            try:
                CurrencyExchangeRateHistoryService().add(validated_data)
            except Exception as e:
                return Response(status=HTTP_400_BAD_REQUEST, data=e)
            return Response(status=HTTP_201_CREATED)
