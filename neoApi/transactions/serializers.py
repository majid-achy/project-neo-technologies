from rest_framework import serializers
from .models import Transaction, Client


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [ 'transaction_id', 'client_id', 'transaction_type', 'transaction_date', 'amount', 'currency']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [ 'client_id', 'name', 'email', 'date_of_birth', 'country', 'account_balance' ]

class ClientTransactionsRequestSerializer(serializers.Serializer):
    client_id = serializers.IntegerField(required=True)
    start_transaction_date = serializers.DateTimeField(required=False)
    end_transaction_date = serializers.DateTimeField(required=False)

    def validate(self, data):
        if 'start_transaction_date' in data and 'end_transaction_date' in data:
            if data['start_transaction_date'] > data['end_transaction_date']:
                raise serializers.ValidationError("End Transaction Date must occur after Start Transaction Date")
        return data