from datetime import date
from django.conf import settings
from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("screening", "Screening"),
        ("interviewing", "Interviewing"),
        ("offered", "Offered"),
        ("rejected", "Rejected"),
        ("ghosted", "Ghosted"),
        ("withdrawn", "Withdrawn"),
    ]
    WORK_TYPE_CHOICES = [
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
        ("onsite", "On-site"),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_applications",
    )
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    work_type = models.CharField(
        max_length=20,
        choices=WORK_TYPE_CHOICES,
        blank=True,
    )
    salary_min = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    salary_max = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied",
    )
    source = models.CharField(
        max_length=100,
        blank=True,
        help_text="Where you found the job, e.g. LinkedIn, company website.",
    )
    notes = models.TextField(null=True, blank=True)
    date_applied = models.DateField(default=date.today)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class StatusHistory(models.Model):
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name="status_history",
    )
    old_status = models.CharField(max_length=20, blank=True)
    new_status = models.CharField(max_length=20)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-changed_at"]

    def __str__(self):
        return f"{self.application} → {self.new_status}"


class Interview(models.Model):
    INTERVIEW_TYPE_CHOICES = [
        ("phone", "Phone"),
        ("video", "Video"),
        ("onsite", "On-site"),
        ("technical", "Technical"),
        ("behavioral", "Behavioral"),
        ("final", "Final"),
        ("other", "Other"),
    ]
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name="interviews",
    )
    interview_type = models.CharField(
        max_length=20,
        choices=INTERVIEW_TYPE_CHOICES,
        default="video",
    )
    scheduled_at = models.DateTimeField()
    meeting_link = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["scheduled_at"]

    def __str__(self):
        return f"{self.application} - {self.interview_type}"