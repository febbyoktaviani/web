from django.conf.urls import include, url

from rest_framework import routers

from django.conf import settings

from . import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^currencies/$', views.CurrencyListView.as_view()),
    url(r'^currency-exchange/$', views.CurrencyExchangeListCreateView.as_view()),
    url(r'^exchange-track/$', views.CurrencyExchangeRateHistoryListView.as_view()),
]