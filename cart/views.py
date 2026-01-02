from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CartItem

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = CartItem.objects.filter(user=request.user)
        data = [
            {
                "product": item.product.name,
                "quantity": item.quantity
            } for item in items
        ]
        return Response(data)
