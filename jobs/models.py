from datetime import date
from django.db import models

from django.conf import settings

# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interviewing', 'Interviewing'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
        ('ghosted', 'Ghosted'),
        ('withdrawn', 'Withdrawn'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )
    notes = models.TextField(null=True, blank=True)
    date_applied = models.DateField(default=date.today) # by default, it will be the date the user fills up the form; can be overriden
    interview_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"