from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import CustomUserCreateView, LogoutViewWithBlacklistTokenReset


def test_create_user_by_api(db, api_rf):
    url = "/api/v1/users/create/"
    view = CustomUserCreateView.as_view()
    new_user = {"email": "d@d.pl", "password": "abcdesfg"}

    request = api_rf.post(url, new_user, format="json")
    request2 = api_rf.post(url, new_user, format="json")

    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get("email") == "d@d.pl"
    assert len(response.data.get("id")) != ""


def test_create_user_by_api_duplicate_error(db, api_rf):
    url = "/api/v1/users/create/"
    view = CustomUserCreateView.as_view()
    new_user = {"email": "d@d.pl", "password": "abcdesfg"}

    request = api_rf.post(url, new_user, format="json")
    request2 = api_rf.post(url, new_user, format="json")

    response = view(request)
    response2 = view(request2)

    assert response2.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_by_api_invalid_email(db, api_rf):
    url = "/api/v1/users/create/"
    view = CustomUserCreateView.as_view()
    new_user = {"email": "d.pl", "password": "abcdesfg"}

    request = api_rf.post(url, new_user, format="json")
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_by_api_invalid_password(db, api_rf):
    url = "/api/v1/users/create/"
    view = CustomUserCreateView.as_view()
    new_user = {"email": "test@test.pl"}
    request = api_rf.post(url, new_user, format="json")
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login_user_by_api_invalid_credentials(db, api_rf):
    url = "/api/v1/users/token/"
    view = TokenObtainPairView.as_view()
    new_user = {"email": "test@test.pl", "password": "abcdesfg"}
    request = api_rf.post(url, new_user, format="json")
    response = view(request)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data.get("detail") == "No active account found with the given credentials"


def test_login_user_by_api_create_and_token_endpoint_success(db, api_rf):
    url_create = "/api/v1/users/create/"
    url_login = "/api/v1/users/token/"
    url_refresh = "/api/v1/users/token/refresh/"
    url_verify = "/api/v1/users/token/verify/"
    url_logout = "/api/v1/users/token/logout/"

    view_create = CustomUserCreateView.as_view()
    view_login = TokenObtainPairView.as_view()
    view_refresh = TokenRefreshView.as_view()
    view_verify = TokenVerifyView.as_view()
    view_logout = LogoutViewWithBlacklistTokenReset.as_view()

    new_user = {"email": "test@test.pl", "password": "test"}

    request_create = api_rf.post(url_create, new_user, format="json")
    request_login = api_rf.post(url_login, new_user, format="json")

    response_create = view_create(request_create)
    response_login = view_login(request_login)

    request_refresh = api_rf.post(url_refresh, {"refresh": response_login.data.get("refresh")}, format="json")
    response_refresh = view_refresh(request_refresh)

    request_verify = api_rf.post(url_verify, {"token": response_refresh.data.get("refresh")}, format="json")
    response_verify = view_verify(request_verify)

    request_logout = api_rf.post(url_logout, {"refresh": response_refresh.data.get("refresh")}, format="json")
    response_logout = view_logout(request_logout)

    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data.get("email") != ""
    assert response_login.status_code == status.HTTP_200_OK
    assert response_login.data.get("access") != ""
    assert response_login.data.get("refresh") != ""
    assert response_refresh.status_code == status.HTTP_200_OK
    assert response_refresh.data.get("access") != ""
    assert response_refresh.data.get("refresh") != ""
    assert response_verify.status_code == status.HTTP_200_OK
    assert response_logout.status_code == status.HTTP_205_RESET_CONTENT


def test_login_user_by_api_create_and_token_endpoint_fail(db, api_rf):
    url_login = "/api/v1/users/token/"
    url_refresh = "/api/v1/users/token/refresh/"
    url_verify = "/api/v1/users/token/verify/"
    url_logout = "/api/v1/users/token/logout/"

    view_login = TokenObtainPairView.as_view()
    view_refresh = TokenRefreshView.as_view()
    view_verify = TokenVerifyView.as_view()
    view_logout = LogoutViewWithBlacklistTokenReset.as_view()

    new_user = {"email": "test@test.pl", "password": "test"}

    request_login = api_rf.post(url_login, new_user, format="json")
    request_refresh = api_rf.post(url_refresh, {"refresh": "test"}, format="json")
    request_verify = api_rf.post(url_verify, {"token": "test"}, format="json")
    request_logout = api_rf.post(url_logout, {"refresh": "test"}, format="json")

    response_login = view_login(request_login)
    response_refresh = view_refresh(request_refresh)
    response_verify = view_verify(request_verify)
    response_logout = view_logout(request_logout)

    assert response_login.status_code == status.HTTP_401_UNAUTHORIZED
    assert response_refresh.status_code == status.HTTP_401_UNAUTHORIZED
    assert response_verify.status_code == status.HTTP_401_UNAUTHORIZED
    assert response_login.data.get("detail") == "No active account found with the given credentials"
    assert response_refresh.data.get("detail") == "Token is invalid or expired"
    assert response_verify.data.get("detail") == "Token is invalid or expired"
    assert response_logout.status_code == status.HTTP_400_BAD_REQUEST
