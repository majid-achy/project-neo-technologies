from django.db import models

class Client(models.Model):
    client_id = models.IntegerField(primary_key= True)
    name = models.CharField()
    email = models.CharField()
    date_of_birth = models.DateField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    account_balance = models.DecimalField(max_digits=8, decimal_places= 2)

class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key= True)
    client_id = models.IntegerField()
    transaction_type = models.CharField()
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=7, decimal_places= 2)
    currency = models.CharField()
