from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from jobs.models import JobApplication, StatusHistory

User = get_user_model()

class JobApplicationAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpassword123",
        )

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        self.job = JobApplication.objects.create(
            user=self.user,
            company="Google",
            title="Backend Developer",
            status="applied",
        )

    def test_authenticated_user_can_list_jobs(self):
        response = self.client.get("/api/jobs/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_user_can_create_job(self):
        response = self.client.post(
            "/api/jobs/",
            {
                "company": "Microsoft",
                "title": "Python Developer",
                "status": "applied",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobApplication.objects.count(), 2)

        created_job = JobApplication.objects.get(
            company="Microsoft"
        )

        self.assertEqual(created_job.user, self.user)

    def test_user_cannot_access_another_users_job(self):
        other_job = JobApplication.objects.create(
            user=self.other_user,
            company="Amazon",
            title="Software Engineer",
        )

        response = self.client.get(
            f"/api/jobs/{other_job.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_status_change_creates_history(self):
        self.job.status = "interviewing"

        response = self.client.patch(
            f"/api/jobs/{self.job.id}/",
            {"status": "interviewing"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertTrue(
            StatusHistory.objects.filter(
                application=self.job,
                old_status="applied",
                new_status="interviewing",
            ).exists()
        )

    def test_status_filter(self):
        JobApplication.objects.create(
            user=self.user,
            company="Meta",
            title="Django Developer",
            status="interviewing",
        )

        response = self.client.get(
            "/api/jobs/?status=interviewing"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_search_filter(self):
        response = self.client.get(
            "/api/jobs/?search=Google"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_unauthenticated_user_cannot_access_jobs(self):
        self.client.credentials()

        response = self.client.get("/api/jobs/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )