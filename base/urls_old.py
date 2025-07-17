# from django.urls import path
# from .views import (
#     # getRoute,
#     getProducts,
#     getProduct,
#     MyTokenObtainPairView,
#     getUserProfile,
#     getUsers,
#     registerUser,
# )

# # from rest_framework_simplejwt.views import (
# #     TokenObtainPairView,
# #     TokenRefreshView,
# # )

# urlpatterns = [
#     # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path("users/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
#     #
#     # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     #
#     # path("", getRoute, name="get-route"),
#     #
#     path("users/register/", registerUser, name="register"),
#     #
#     path("users/profile/", getUserProfile, name="Users-profile"),
#     path("users/", getUsers, name="Users"),
#     #
#     path("products/", getProducts, name="products"),
#     path("products/<int:pk>/", getProduct, name="product"),
# ]
