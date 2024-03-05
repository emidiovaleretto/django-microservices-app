from random import choice

from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, User
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = choice(users)
        return Response(
            {"id": user.id}
        )