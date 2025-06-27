from .products import products  # Assuming you have a products.py file with product data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product  # Import your Product model
from .serializers import ProductSerializer  # Import your Product serializer


# Create your views here.
@api_view(["GET"])
def getRoute(request):
    routes = [
        {
            "Endpoint": "/products/",
            "method": "GET",
            "description": "Returns a list of products",
        },
        {
            "Endpoint": "/products/<id>/",
            "method": "GET",
            "description": "Returns a single product by ID",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    # products = [
    #     {
    #         '_id': '1',
    #         'name': 'Sample Product 1',
    #         'image': '/images/sample1.jpg',
    #         'description': 'This is a sample product description.',
    #         'brand': 'Brand A',
    #         'category': 'Category A',
    #         'price': 29.99,
    #         'countInStock': 10,
    #         'rating': 4.5,
    #         'numReviews': 5,
    #     },
    #     # Add more products as needed
    # ]
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    products = serializer.data  # Convert queryset to list of dictionaries
    return Response(products)


@api_view(["GET"])
def getProduct(request, pk):
    # product=Product.objects.filter(id=pk).first()
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    products = serializer.data  # Convert queryset to list of dictionaries
    return Response(products)