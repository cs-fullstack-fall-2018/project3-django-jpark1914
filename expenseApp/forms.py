from .models import AccountModel, UserSetup, TransactionModel
from django import forms

class AccountForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['account_name','balance','savings','date_of_balance']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetup
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),

        }