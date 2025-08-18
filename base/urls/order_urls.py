from django.urls import path

from base.views import order_views as views


urlpatterns = [
    path("", views.getOrders, name="orders"),
    path("add/", views.addOrderItems, name="orders-add"),
    path("myorders/", views.getMyOrders, name="myorders"),
    path("<str:pk>/deliver/", views.updateOrderToDelivered, name="order-delivered"),
    path("<str:pk>/", views.getOrderById, name="user-order"),
    path("<str:pk>/pay/", views.updateOrderToPaid, name="pay"),
    # path("create-order/", views.create_order, name="create_order"),
    # path("verify-payment/", views.verify_payment, name="verify_payment"),
    path("orders/<str:pk>/", views.getOrderDetails, name="order-details"),
]
