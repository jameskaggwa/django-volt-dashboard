from django.contrib import admin


# admin.py
from django.contrib import admin
from .models import Journal, TradingAccount
from .forms import JournalForm, TradingAccountForm


class JournalAdmin(admin.ModelAdmin):
    form = JournalForm


class TradingAccountAdmin(admin.ModelAdmin):
    form = TradingAccountForm


admin.site.register(Journal, JournalAdmin)
admin.site.register(TradingAccount, TradingAccountAdmin)
