from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from jobs.models import JobApplication, Interview


User = get_user_model()


class InterviewAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="interviewuser",
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
        )

    def test_user_can_create_interview(self):
        response = self.client.post(
            "/api/interviews/",
            {
                "application": self.job.id,
                "interview_type": "technical",
                "scheduled_at": (
                    timezone.now() + timedelta(days=2)
                ).isoformat(),
                "meeting_link": "https://example.com/meeting",
                "notes": "Technical round",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Interview.objects.count(),
            1,
        )

    def test_user_can_list_interviews(self):
        Interview.objects.create(
            application=self.job,
            interview_type="video",
            scheduled_at=timezone.now() + timedelta(days=1),
        )

        response = self.client.get("/api/interviews/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            1,
        )