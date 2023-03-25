from django.db import models
from django.contrib.auth.models import User


class TradingAccount(models.Model):
    name = models.CharField(max_length=50)
    date_opened = models.DateField()
    amount_opened_with = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    broker = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Journal(models.Model):
    # Define the most commonly traded currency pairs as choices
    PAIR_CHOICES = [
        ('EUR/USD', 'EUR/USD'),
        ('USD/JPY', 'USD/JPY'),
        ('GBP/USD', 'GBP/USD'),
        ('USD/CHF', 'USD/CHF'),
        ('AUD/USD', 'AUD/USD'),
        ('USD/CAD', 'USD/CAD'),
        ('NZD/USD', 'NZD/USD'),
        ('EUR/GBP', 'EUR/GBP'),
        ('EUR/JPY', 'EUR/JPY'),
        ('GBP/JPY', 'GBP/JPY'),
        ('CHF/JPY', 'CHF/JPY'),
        ('AUD/JPY', 'AUD/JPY'),
        ('CAD/JPY', 'CAD/JPY'),
        ('NZD/JPY', 'NZD/JPY'),
        ('GBP/CHF', 'GBP/CHF'),
        ('EUR/CAD', 'EUR/CAD'),
        ('EUR/AUD', 'EUR/AUD'),
        ('AUD/CAD', 'AUD/CAD'),
        ('AUD/NZD', 'AUD/NZD'),
        ('NZD/CAD', 'NZD/CAD'),
        ('EUR/CHF', 'EUR/CHF'),
        ('USD/HKD', 'USD/HKD'),
        ('USD/MXN', 'USD/MXN'),
        ('USD/SGD', 'USD/SGD'),
        ('USD/TRY', 'USD/TRY'),
        ('USD/ZAR', 'USD/ZAR'),
    ]

    POSITION_CHOICES = [
        ('LONG', 'LONG'),
        ('SHORT', 'SHORT')
    ]

    pair = models.CharField(max_length=10, choices=PAIR_CHOICES)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True, blank=True)
    lot = models.DecimalField(max_digits=10, decimal_places=5)
    is_open = models.BooleanField()
    take_profit = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    stop_loss = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    spread = models.DecimalField(max_digits=10, decimal_places=5)
    entry_price = models.DecimalField(max_digits=10, decimal_places=5)
    exit_price = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    strategy = models.CharField(max_length=50)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_profit = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    risk_ratio = models.DecimalField(max_digits=10, decimal_places=2)
    pips = models.IntegerField()
    conviction = models.CharField(max_length=50)
    trading_acct = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    time_frame = models.CharField(max_length=10)
    is_tp_hit = models.BooleanField()

    def __str__(self):
        return self.pair
