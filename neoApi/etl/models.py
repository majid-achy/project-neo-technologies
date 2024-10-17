from django.db import models

class ClientError(models.Model):
    job_id = models.CharField()
    client_id = models.IntegerField()
    name = models.CharField()
    email = models.CharField()
    date_of_birth = models.DateField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    account_balance = models.DecimalField(max_digits=8, decimal_places= 2)
    error = models.CharField()

class TransactionError(models.Model):
    job_id = models.CharField()
    transaction_id = models.IntegerField()
    client_id = models.IntegerField()
    transaction_type = models.CharField()
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=7, decimal_places= 2)
    currency = models.CharField()
    error = models.CharField()

class JobExecution(models.Model):
    job_id = models.CharField(primary_key=True)
    job_name = models.CharField()
    successful_records = models.IntegerField()
    failed_records = models.IntegerField()


