from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from jobs.models import JobApplication


User = get_user_model()


class DashboardAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="dashboarduser",
            password="testpassword123",
        )

        refresh = RefreshToken.for_user(self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        JobApplication.objects.create(
            user=self.user,
            company="Google",
            title="Backend Developer",
            status="applied",
        )

        JobApplication.objects.create(
            user=self.user,
            company="Microsoft",
            title="Python Developer",
            status="interviewing",
        )

        JobApplication.objects.create(
            user=self.user,
            company="Amazon",
            title="Software Engineer",
            status="rejected",
        )

    def test_dashboard_returns_statistics(self):
        response = self.client.get(
            "/api/dashboard/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["total_applications"],
            3,
        )

        self.assertEqual(
            response.data["active_applications"],
            2,
        )

        self.assertEqual(
            response.data["rejected"],
            1,
        )

        self.assertEqual(
            response.data["by_status"]["applied"],
            1,
        )

        self.assertEqual(
            response.data["by_status"]["interviewing"],
            1,
        )