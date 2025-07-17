from django.urls import path
from base.views import user_views as views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    #
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #
    # path("", getRoute, name="get-route"),
    #
    path("register/", views.registerUser, name="register"),
    #
    path("profile/", views.getUserProfile, name="Users-profile"),
    path("", views.getUsers, name="Users"),
]
