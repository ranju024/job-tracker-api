from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewset, DashboardView, InterviewViewSet, StatusHistoryViewSet

router = DefaultRouter() # Instantiates a router that automatically creates URL patterns for your API. 
router.register(r'jobs', JobApplicationViewset, basename='job')
router.register(r'interviews', InterviewViewSet, basename='interview')
router.register(r'status-history', StatusHistoryViewSet, basename='status-history')

urlpatterns = router.urls + [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]