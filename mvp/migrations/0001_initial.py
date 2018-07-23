# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('udate', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=5, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'currency',
            },
        ),
        migrations.CreateModel(
            name='CurrencyExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('udate', models.DateTimeField(auto_now=True)),
                ('source_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_currency', to='mvp.Currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency', to='mvp.Currency')),
            ],
            options={
                'db_table': 'currency_exchange',
            },
        ),
        migrations.CreateModel(
            name='CurrencyExchangeRateHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('udate', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('rate', models.FloatField()),
                ('currency_exchange', models.ForeignKey(db_column='currency_exchange_id', on_delete=django.db.models.deletion.CASCADE, to='mvp.CurrencyExchange')),
            ],
            options={
                'db_table': 'currency_exchange_rate_history',
            },
        ),
        migrations.AlterUniqueTogether(
            name='currencyexchange',
            unique_together=set([('source_currency', 'target_currency')]),
        ),
    ]