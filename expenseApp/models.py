from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class UserSetup(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=257)
    email = models.EmailField()

    def __str__(self):
        return self.name


class AccountModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    account_name = models.CharField(max_length=200, default='', null=True, blank=True)
    balance = models.FloatField(default=0, null=True, blank=True)
    checking = models.FloatField(default=0, null=True, blank=True)
    savings= models.FloatField(default=0, null=True, blank=True)
    deposit = models.FloatField(default=0, null=True, blank=True)
    expense = models.FloatField(default=0, null=True, blank=True)
    date_of_balance = models.DateField(default=timezone.now)

    def __str__(self):
        return self.account_name





class TransactionModel(models.Model):
    amount = models.FloatField(default=0, null=True, blank=True)
    time_of_transaction = models.DateField(default=timezone.now)
    transaction =models.CharField(max_length=200, default='Main Account', null=True, blank=True)
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.amount

