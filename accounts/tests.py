from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterAPITestCase(APITestCase):
    def test_user_can_register(self):
        response = self.client.post(
            "/api/accounts/register/",
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password": "strongpassword123",
                "password2": "strongpassword123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())
        # password must never be echoed back
        self.assertNotIn("password", response.data)

    def test_registration_fails_on_password_mismatch(self):
        response = self.client.post(
            "/api/accounts/register/",
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password": "strongpassword123",
                "password2": "differentpassword",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_registration_fails_on_duplicate_username(self):
        User.objects.create_user(username="taken", password="testpassword123")

        response = self.client.post(
            "/api/accounts/register/",
            {
                "username": "taken",
                "email": "another@example.com",
                "password": "strongpassword123",
                "password2": "strongpassword123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="loginuser",
            password="testpassword123",
        )

    def test_user_can_login_with_valid_credentials(self):
        response = self.client.post(
            "/api/accounts/login/",
            {
                "username": "loginuser",
                "password": "testpassword123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_fails_with_invalid_credentials(self):
        response = self.client.post(
            "/api/accounts/login/",
            {
                "username": "loginuser",
                "password": "wrongpassword",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LogoutAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="logoutuser",
            password="testpassword123",
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}"
        )

    def test_user_can_logout(self):
        response = self.client.post(
            "/api/accounts/logout/",
            {"refresh": str(self.refresh)},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_blacklisted_refresh_token_cannot_be_reused(self):
        self.client.post(
            "/api/accounts/logout/",
            {"refresh": str(self.refresh)},
            format="json",
        )

        response = self.client.post(
            "/api/accounts/token/refresh/",
            {"refresh": str(self.refresh)},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_without_refresh_token_fails(self):
        response = self.client.post(
            "/api/accounts/logout/",
            {},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)