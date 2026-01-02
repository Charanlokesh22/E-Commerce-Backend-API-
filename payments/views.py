import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))

class CreatePayment(APIView):
    def post(self, request):
        order = client.order.create({
            "amount": int(request.data["amount"]) * 100,
            "currency": "INR",
            "payment_capture": 1
        })
        return Response(order)
