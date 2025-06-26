from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating) + " - " + self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt) + " - " + str(self.user.username)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name) + " - " + str(self.order._id)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address) + " - " + str(self.order._id)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     email = models.EmailField(max_length=200, null=True, blank=True)
#     password = models.CharField(max_length=200, null=True, blank=True)
#     isAdmin = models.BooleanField(default=False)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.user.username) + " - " + str(self.name)


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to="product_images/", null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - Image"


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.user.username)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.quantity)
#         )


# class Wishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     added_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.user.username) + " - " + str(self.product.name)


# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     message = models.CharField(max_length=255, null=True, blank=True)
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.user.username) + " - " + str(self.message)


# class ReviewImage(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to="review_images/", null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.review.product.name) + " - Review Image"


# class ProductCategory(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return self.name


# class ProductCategoryMapping(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.category.name)


# class ProductTag(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return self.name


# class ProductTagMapping(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE, null=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.tag.name)


# class ProductVariant(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     stock = models.IntegerField(null=True, blank=True, default=0)
#     sku = models.CharField(max_length=200, unique=True, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.name)


# class ProductVariantImage(models.Model):
#     variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to="variant_images/", null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.variant.product.name) + " - Variant Image"


# class ProductReview(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     rating = models.IntegerField(null=True, blank=True, default=0)
#     comment = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.product.name)
#             + " - "
#             + str(self.rating)
#             + " - "
#             + str(self.user.username)
#         )


# class ProductReviewImage(models.Model):
#     review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to="review_images/", null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.review.product.name) + " - Review Image"


# class ProductDiscount(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     discount_percentage = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True, blank=True
#     )
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.discount_percentage) + "%"


# class ProductStockHistory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity_change = models.IntegerField(null=True, blank=True)
#     change_date = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.quantity_change) + " units"


# class ProductPriceHistory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     price_change = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True
#     )
#     change_date = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.price_change) + " units"


# class ProductSEO(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
#     meta_title = models.CharField(max_length=200, null=True, blank=True)
#     meta_description = models.TextField(null=True, blank=True)
#     meta_keywords = models.CharField(max_length=500, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - SEO"


# class ProductFAQ(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     question = models.CharField(max_length=500, null=True, blank=True)
#     answer = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - " + str(self.question)


# class ProductSpecification(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     spec_name = models.CharField(max_length=200, null=True, blank=True)
#     spec_value = models.CharField(max_length=500, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.product.name)
#             + " - "
#             + str(self.spec_name)
#             + ": "
#             + str(self.spec_value)
#         )


# class ProductBundle(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     products = models.ManyToManyField(Product, related_name="bundles", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.name) + " - " + str(self.description)


# class ProductBundleItem(models.Model):
#     bundle = models.ForeignKey(ProductBundle, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField(default=1)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.bundle.name)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.quantity)
#         )


# class ProductComparison(models.Model):
#     product1 = models.ForeignKey(
#         Product, related_name="comparison_product1", on_delete=models.CASCADE, null=True
#     )
#     product2 = models.ForeignKey(
#         Product, related_name="comparison_product2", on_delete=models.CASCADE, null=True
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return f"{self.product1.name} vs {self.product2.name}"


# class ProductWishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     added_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.user.username) + " - " + str(self.product.name)


# class ProductSearchHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     search_query = models.CharField(max_length=500, null=True, blank=True)
#     search_date = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.user.username) + " - " + str(self.search_query)


# class ProductRecommendation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     recommendation_reason = models.CharField(max_length=500, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.user.username)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.recommendation_reason)
#         )


# class ProductAlert(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     alert_type = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'price drop', 'back in stock'
#     alert_value = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True
#     )  # e.g., target price for price drop alerts
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.user.username)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.alert_type)
#         )


# class ProductReturn(models.Model):
#     order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
#     reason = models.TextField(null=True, blank=True)
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     requested_at = models.DateTimeField(auto_now_add=True)
#     processed_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.order_item.product.name) + " - " + str(self.status)


# class ProductReturnItem(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturn, on_delete=models.CASCADE, null=True
#     )
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField(default=1)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.return_request.order_item.product.name)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.quantity)
#         )


# class ProductReturnStatus(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturn, on_delete=models.CASCADE, null=True
#     )
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     updated_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.return_request.order_item.product.name) + " - " + str(self.status)
#         )


# class ProductReturnHistory(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturn, on_delete=models.CASCADE, null=True
#     )
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     updated_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.return_request.order_item.product.name) + " - " + str(self.status)
#         )


# class ProductReturnPolicy(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     policy_text = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - Return Policy"


# class ProductReturnRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     reason = models.TextField(null=True, blank=True)
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     requested_at = models.DateTimeField(auto_now_add=True)
#     processed_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.user.username)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.status)
#         )


# class ProductReturnRequestItem(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturnRequest, on_delete=models.CASCADE, null=True
#     )
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField(default=1)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return (
#             str(self.return_request.user.username)
#             + " - "
#             + str(self.product.name)
#             + " - "
#             + str(self.quantity)
#         )


# class ProductReturnRequestStatus(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturnRequest, on_delete=models.CASCADE, null=True
#     )
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     updated_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.return_request.user.username) + " - " + str(self.status)


# class ProductReturnRequestHistory(models.Model):
#     return_request = models.ForeignKey(
#         ProductReturnRequest, on_delete=models.CASCADE, null=True
#     )
#     status = models.CharField(
#         max_length=200, null=True, blank=True
#     )  # e.g., 'pending', 'approved', 'rejected'
#     updated_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.return_request.user.username) + " - " + str(self.status)


# class ProductReturnRequestPolicy(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     policy_text = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.product.name) + " - Return Request Policy"
