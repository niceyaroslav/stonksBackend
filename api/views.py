from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.FinanceService import asset_tracker
from api.models import Transaction
from api.serializers import TransactionSerializer


class RegistrationApiView(APIView):

    def post(self, request):
        data = request.data
        User.objects.create_user(data.get('username'),
                                 data.get('email'),
                                 data.get('password'))
        return Response('Registration successful!')


class UserDataApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Response({"username": user.username,
                         "first_name": user.first_name,
                         "last_name": user.last_name,
                         "email": user.email})


class YahooAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(asset_tracker.get_asset_info(request.GET.get('asset')))


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

        if not amount_crypto:
            try:
                amount_crypto = float(amount_cash) / asset_tracker.get_asset_price_at_timepoint(asset, dot)
            except IndexError:
                amount_crypto = 0

        serializer.save(amount_crypto=amount_crypto, user=self.request.user)


class TransactionDetailsApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


