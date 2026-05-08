from rest_framework import viewsets, permissions
from .models import JobApplication
from .serializers import JobApplicationSerializer

# Create your views here.
class JobApplicationViewset(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated] # ensures only authenticated user with
    # valid jwt token can access this view

    def get_queryset(self):
        # only returns the current user's applications
        return JobApplication.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # add user_id when a new application is added
        serializer.save(user=self.request.user)

