from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, pagination
from .models import Transaction
from .serializers import TransactionSerializer, ClientTransactionsRequestSerializer


# Create your views here.
@api_view(['Get'])
def get_transactions(request):
    client_transaction_request = ClientTransactionsRequestSerializer(data=request.query_params)
    client_transaction_request.is_valid(raise_exception=True)
    if 'start_transaction_date' in request.query_params and 'end_transaction_date' in request.query_params:
        transactions = Transaction.objects.filter(client_id = request.query_params["client_id"], transaction_date__gte = request.query_params["start_transaction_date"], transaction_date__lte = request.query_params["end_transaction_date"])
    elif 'start_transaction_date' in request.query_params:
        transactions = Transaction.objects.filter(client_id = request.query_params["client_id"], transaction_date__gte = request.query_params["start_transaction_date"])
    elif 'end_transaction_date' in request.query_params:
        transactions = Transaction.objects.filter(client_id = request.query_params["client_id"], transaction_date__lte = request.query_params["end_transaction_date"])
    else:
        transactions = Transaction.objects.filter(client_id = request.query_params["client_id"])
    paginator = pagination.LimitOffsetPagination()
    paginator.default_limit = 10
    result_page = paginator.paginate_queryset(transactions, request)
    serializer = TransactionSerializer(result_page, many=True)
    # transactions_serializer = TransactionSerializer(transactions, many= True)
    return paginator.get_paginated_response(serializer.data)
    # else:
    #     return Response({"error": "test"}, status= status.HTTP_400_BAD_REQUEST)