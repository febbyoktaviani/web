from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.status import HTTP_400_BAD_REQUEST

from .services import CurrencyService
from .views import CurrencyListView
from .views import CurrencyExchangeListCreateView
from .views import CurrencyExchangeRateHistoryListView

factory = APIRequestFactory()


class TestCurrencyListView(TestCase):

    def test_get_list(self):

        view = CurrencyListView.as_view()

        # Make request
        request = factory.get('/currencies/')
        response = view(request)

        self.assertEqual(response.status_code, HTTP_200_OK, 'status success' )


class TestCurrencyExchangeListCreateView(TestCase):
    def test_get_list(self):
        view = CurrencyExchangeListCreateView.as_view()

        # Make request
        request = factory.get('/currency-exchange/')
        response = view(request)

        self.assertEqual(response.status_code, HTTP_200_OK, 'status success' )


    def test_post(self):
        view = CurrencyExchangeListCreateView.as_view()
        data1 = {
            "source_currency": 2,
            "target_currency": 1,
        }

        data2 = {
            "target_currency": 1,
        }


        # test HTTP_201_CREATED
        request1 = factory.post('/exchange-currency/', data1, format='json')
        response1 = view(request1)
        self.assertEqual(response1.status_code, HTTP_201_CREATED)

        # test BAD Request
        request2 = factory.post('/exchange-currency/', data2, format='json')
        response2 = view(request2)
        self.assertEqual(response2.status_code, HTTP_400_BAD_REQUEST)

    # def test_delete(self):
    #     view = CurrencyExchangeListCreateView.as_view()
    #     data = {
    #         "source_currency": 2,
    #         "target_currency": 1
    #     }

    #     # TEST HTTP_202_ACCEPTED (delete)
    #     request = factory.delete('/exchange-currency/', data, format='json')
    #     response = view(request)
    #     self.assertEqual(response.status_code, HTTP_202_ACCEPTED)


# class TestCurrencyExchangeRateHistoryListView(TestCase):
#     def test_post(self):
#         view = CurrencyExchangeRateHistoryListView.as_view()
#         data1 = {
#             "source_currency": 2,
#             "target_currency": 1,
#             "date": "2018-07-19",
#             "rate": 1.3456
#         }

#         data2 = {
#             "target_currency": 1,
#             "date": "2018-07-22",
#             "rate": 1.3456
#         }

#         data3 = {
#             "source_currency": 2,
#             "target_currency": 1,
#             "date": "2018-07-22",
#         }

#         # test HTTP_201_CREATED
#         request1 = factory.post('/exchange-track/', data1, format='json')
#         response1 = view(request1)
#         print(response1)
#         self.assertEqual(response1.status_code, HTTP_201_CREATED)

#         # test BAD Request
#         request2 = factory.post('/exchange-track/', data2, format='json')
#         response2 = view(request2)
#         self.assertEqual(response2.status_code, HTTP_400_BAD_REQUEST)