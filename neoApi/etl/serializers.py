from rest_framework import serializers
from .models import TransactionError, ClientError


class TransactionErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionError
        fields = [ 'job_id', 'transaction_id', 'client_id', 'transaction_type', 'transaction_date', 'amount', 'currency', 'error']

class ClientErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientError
        fields = [ 'job_id', 'client_id', 'name', 'email', 'date_of_birth', 'country', 'account_balance', 'error' ]