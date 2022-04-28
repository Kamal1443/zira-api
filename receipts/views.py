from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Receipt
from .serializers import ReceiptSerializer

# Create your views here.

class Rec_get(APIView):
    def get(self, request):
        all_receipts = Receipt.objects.all()

        serialized_recs = ReceiptSerializer(data=all_receipts, many=True)
        serialized_recs.is_valid()

        return Response(serialized_recs.data)
