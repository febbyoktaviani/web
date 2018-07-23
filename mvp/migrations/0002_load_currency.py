from __future__ import unicode_literals

from django.db import migrations


def load_currency(apps, schema_editor):
    currency_list = [
        ('Afghan afghani', 'AFN'),
        ('European euro', 'EUR'),
        ('Albanian lek', 'ALL'),
        ('Algerian dinar', 'DZD'),
        ('United States dollar', 'USD'),
        ('Angolan kwanza', 'AOA'),
        ('East Caribbean dollar', 'XCD'),
        ('Argentine peso', 'ARS'),
        ('Indonesian rupiah', 'IDR'),
        ('Japanese Yen', 'JPY'),
        ('Pound sterling', 'GBP'),
    ]

    Currency = apps.get_model("mvp", "Currency")
    for description, name in currency_list:
        currency = Currency(description=description, name=name)
        currency.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_currency),
    ]