from django.urls import path
from base.views import  product_views as views
# from ..views import user_views as views

urlpatterns = [
    path("", views.getProducts, name="products"),
    path("<int:pk>/", views.getProduct, name="product"),
]
