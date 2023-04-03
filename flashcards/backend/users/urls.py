from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CustomUserCreateView, CustomUserLogoutViewWithBlacklistTokenReset, CustomUserUpdatePasswordView

app_name = "users"

urlpatterns = [
    path("users/register/", CustomUserCreateView.as_view(), name="register"),
    path("users/change-password/", CustomUserUpdatePasswordView.as_view(), name="change_password"),
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("users/logout/", CustomUserLogoutViewWithBlacklistTokenReset.as_view(), name="logout_user"),
]
