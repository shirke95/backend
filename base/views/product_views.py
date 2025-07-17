from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product  # Import your Product model
from base.serializers import (
    ProductSerializer,
)  # Import your Product serializer


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    products = serializer.data  # Convert queryset to list of dictionaries
    return Response(products)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    products = serializer.data  # Convert queryset to list of dictionaries
    return Response(products)
