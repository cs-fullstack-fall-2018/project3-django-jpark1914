from .models import AccountModel, UserSetup, TransactionModel
from django import forms

class AccountForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['account_name','balance','savings','deposit', 'expense']
        widgets = {'balance': forms.HiddenInput, 'savings':forms.HiddenInput(), 'deposit': forms.HiddenInput(), 'expense': forms.HiddenInput()}


class DepositForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['deposit','expense']
        widgets = {'expense': forms.HiddenInput()}

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['expense']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetup
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
