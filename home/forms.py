# forms.py
from django import forms
from .models import Journal, TradingAccount


class TradingAccountForm(forms.ModelForm):
    class Meta:
        model = TradingAccount
        fields = ['name', 'date_opened',
                  'amount_opened_with', 'balance', 'broker', 'author']


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['pair', 'entry_date', 'exit_date', 'lot', 'is_open', 'take_profit', 'stop_loss',
                  'spread', 'entry_price', 'exit_price', 'strategy', 'position', 'is_profit', 'risk_ratio',
                  'pips', 'conviction', 'trading_acct', 'time_frame', 'is_tp_hit']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['trading_acct'].queryset = TradingAccount.objects.filter(
    #         author=self.instance.author)
