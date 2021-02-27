from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Transaction
from api.serializers import TransactionSerializer
from api.FinanceService import asset_tracker


class RegistrationApiView(APIView):

    def post(self, request):
        data = request.data
        User.objects.create_user(data['username'],
                                 data['email'],
                                 data['password'])
        return Response('Registration successful!')


class TransactionApiView(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        data = self.request.data
        asset = data.get('asset')
        dot = data.get('date_of_transfer')
        amount_crypto = data.get('amount_crypto')
        amount_cash = data.get('amount_cash')
        print(type(amount_cash))
        if not amount_crypto:
            amount_crypto = float(amount_cash) / asset_tracker.get_asset_price_at_timepoint(asset, dot)
        serializer.save(amount_crypto=amount_crypto, user=self.request.user)


class TransactionDetailsApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
