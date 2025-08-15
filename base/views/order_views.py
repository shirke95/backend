import razorpay
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from base.models import Order, OrderItem, Payment, Product, ShippingAddress
from base.serializers import OrderSerializer


# Razorpay client
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data

    orderItems = data["orderItems"]

    if orderItems and len(orderItems) == 0:
        return Response(
            {"detail": "No Order Items"}, status=status.HTTP_400_BAD_REQUEST
        )
    else:

        # (1) Create order

        order = Order.objects.create(
            user=user,
            paymentMethod=data["paymentMethod"],
            taxPrice=data["taxPrice"],
            shippingPrice=data["shippingPrice"],
            totalPrice=data["totalPrice"],
        )

        # (2) Create shipping address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data["shippingAddress"]["address"],
            city=data["shippingAddress"]["city"],
            postalCode=data["shippingAddress"]["postalCode"],
            country=data["shippingAddress"]["country"],
        )

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            product = Product.objects.get(_id=i["product"])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i["qty"],
                price=i["price"],
                image=product.image.url,
            )

            # (4) Update stock

            product.countInStock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getMyOrders(request):
#     user = request.user
#     orders = user.order_set.all()
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def getOrders(request):
#     orders = Order.objects.all()
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):

    user = request.user

    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response(
                {"detail": "Not authorized to view this order"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except:
        return Response(
            {"detail": "Order does not exist"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(_id=pk)

    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()

    return Response("Order was paid")


# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def updateOrderToDelivered(request, pk):
#     order = Order.objects.get(_id=pk)

#     order.isDelivered = True
#     order.deliveredAt = datetime.now()
#     order.save()

#     return Response('Order was delivered')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request):
    try:
        amount = int(request.data.get("amount")) * 100  # amount in paise
        currency = "INR"

        # Create Razorpay order
        razorpay_order = razorpay_client.order.create(
            {"amount": amount, "currency": currency, "payment_capture": 1}
        )

        # Save to DB
        payment = Payment.objects.create(
            user=request.user,
            order_id=razorpay_order["id"],
            amount=request.data.get("amount"),
            currency=currency,
            status="created",
        )

        return Response(
            {
                "order_id": razorpay_order["id"],
                "amount": amount,
                "currency": currency,
                "key": settings.RAZORPAY_KEY_ID,
            },
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    try:
        order_id = request.data.get("order_id")
        payment_id = request.data.get("payment_id")
        signature = request.data.get("signature")

        params_dict = {
            "razorpay_order_id": order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature,
        }

        # Verify signature
        razorpay_client.utility.verify_payment_signature(params_dict)

        # Update DB
        payment = Payment.objects.get(order_id=order_id)
        payment.payment_id = payment_id
        payment.signature = signature
        payment.status = "paid"
        payment.save()

        return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
    except razorpay.errors.SignatureVerificationError:
        return Response(
            {"error": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST
        )
