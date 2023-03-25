from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Journal, TradingAccount


@receiver(pre_save, sender=Journal)
def set_journal_author(sender, instance, **kwargs):
    if not instance.author:
        instance.author = User.objects.get(username='some_default_username')
        # replace `some_default_username` with the actual username of the default author
    # Check if the user is authenticated
    if instance.author.is_authenticated:
        instance.author = instance.author
    else:
        instance.author = None


@receiver(pre_save, sender=TradingAccount)
def set_trading_acct_author(sender, instance, **kwargs):
    if not instance.author:
        instance.author = User.objects.get(username='some_default_username')
        # replace `some_default_username` with the actual username of the default author
    # Check if the user is authenticated
    if instance.author.is_authenticated:
        instance.author = instance.author
    else:
        instance.author = None
