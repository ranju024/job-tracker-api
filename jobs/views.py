from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema

from .models import JobApplication, StatusHistory, Interview
from .serializers import (
    JobApplicationSerializer,
    StatusHistorySerializer,
    InterviewSerializer,
)
from .pagination import JobPagination

@extend_schema(tags=["Job Applications"])
class JobApplicationViewset(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = JobPagination

    def get_queryset(self):
        queryset = JobApplication.objects.filter(
            user=self.request.user
        ).prefetch_related(
            "status_history",
            "interviews",
        )

        status_filter = self.request.query_params.get("status")
        company = self.request.query_params.get("company")
        location = self.request.query_params.get("location")
        work_type = self.request.query_params.get("work_type")
        search = self.request.query_params.get("search")

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        if company:
            queryset = queryset.filter(
                company__icontains=company
            )

        if location:
            queryset = queryset.filter(
                location__icontains=location
            )

        if work_type:
            queryset = queryset.filter(
                work_type=work_type
            )

        if search:
            queryset = queryset.filter(
                Q(company__icontains=search)
                | Q(title__icontains=search)
            )

        ordering = self.request.query_params.get(
            "ordering",
            "-created_at",
        )

        allowed_ordering = [
            "created_at",
            "-created_at",
            "date_applied",
            "-date_applied",
            "company",
            "-company",
            "updated_at",
            "-updated_at",
        ]

        if ordering in allowed_ordering:
            queryset = queryset.order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        application = serializer.save(user=self.request.user)

        StatusHistory.objects.create(
            application=application,
            old_status="",
            new_status=application.status,
        )

    def perform_update(self, serializer):
        old_status = serializer.instance.status
        application = serializer.save()
        if old_status != application.status:
            StatusHistory.objects.create(
                application=application,
                old_status=old_status,
                new_status=application.status,
            )

@extend_schema(tags=["Interviews"])
class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interview.objects.filter(
            application__user=self.request.user
        ).select_related("application")

    def perform_create(self, serializer):
        application = serializer.validated_data["application"]

        if application.user != self.request.user:
            raise PermissionDenied(
                "You cannot add an interview to this application."
            )

        serializer.save()

@extend_schema(tags=["Status History"])
class StatusHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatusHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StatusHistory.objects.filter(
            application__user=self.request.user
        ).select_related("application")


@extend_schema(
    tags=["Dashboard"], 
    summary="Get job application dashboard", 
    description=(
        "Returns application statistics, status breakdown, "
        "upcoming interviews, and stale applications."
    ),
)
class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        applications = JobApplication.objects.filter(
            user=request.user
        )

        total = applications.count()

        status_counts = applications.values(
            "status"
        ).annotate(
            count=Count("id")
        )

        by_status = {
            item["status"]: item["count"]
            for item in status_counts
        }

        upcoming_interviews = Interview.objects.filter(
            application__user=request.user,
            scheduled_at__gte=timezone.now(),
        ).select_related(
            "application"
        )[:10]

        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

        stale_applications = applications.filter(
            updated_at__lte=thirty_days_ago,
        ).exclude(
            status__in=["rejected", "withdrawn", "ghosted", "offered"]
        )[:10]

        interviews_count = Interview.objects.filter(
            application__user=request.user
        ).count()

        offers = applications.filter(
            status="offered"
        ).count()

        rejected = applications.filter(
            status="rejected"
        ).count()

        active = applications.exclude(
            status__in=["rejected", "withdrawn", "ghosted", "offered"]
        ).count()

        response_rate = 0

        if total:
            responses = total - applications.filter(
                status__in=["applied", "ghosted"]
            ).count()

            response_rate = round(
                (responses / total) * 100,
                2,
            )

        return Response({
            "total_applications": total,
            "active_applications": active,
            "interviews": interviews_count,
            "offers": offers,
            "rejected": rejected,
            "response_rate": response_rate,
            "by_status": by_status,
            "upcoming_interviews": InterviewSerializer(
                upcoming_interviews,
                many=True,
                context={"request": request},
            ).data,
            "stale_applications": JobApplicationSerializer(
                stale_applications,
                many=True,
                context={"request": request},
            ).data,
        })