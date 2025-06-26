from django.urls import path
from .views import getRoute, getProducts, getProduct


urlpatterns = [
    path("", getRoute, name="get-route"),
    path("products/", getProducts, name="get-products"),
    path("products/<str:pk>/", getProduct, name="get-product"),
]
