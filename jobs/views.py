from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from django.db.models import Count
from django.utils import timezone
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer


# Create your views here.
class JobApplicationViewset(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated] # ensures only authenticated user with
    # valid jwt token can access this view

    def get_queryset(self):
        # only returns the current user's applications
        status = self.request.query_params.get('status')

        if status is None: 
            return JobApplication.objects.filter(user=self.request.user)
        
        return JobApplication.objects.filter(user=self.request.user, status=status)
    
    def perform_create(self, serializer):
        # add user_id when a new application is added
        serializer.save(user=self.request.user)


class DashboardView(APIView):
    def get(self, request):
        user = request.user
        applications = JobApplication.objects.filter(user=user)
        total = applications.count()

        by_status = {}
        status_counts = applications.values('status').annotate(count=Count('id'))
        ''' it returns sth like this => 
            [
                {'status': 'applied', 'count': 8},
                {'status': 'interviewing', 'count': 2},
            ]'''
        for item in status_counts:
            by_status[item['status']] = item['count']  # 'applied': 8

        # upcoming interviews
        upcoming_interviews = applications.filter(
            interview_date__gte = timezone.now().date()).order_by('interview_date')
        

        # stale applications with no update in 30 days
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        stale = applications.filter(
            updated_at__lte = thirty_days_ago
        )

        return Response({
            'total': total,
            'by_status': by_status,
            'upcoming_interviews': JobApplicationSerializer(upcoming_interviews, many=True).data,
            'stale_applications': JobApplicationSerializer(stale, many=True).data,
        })