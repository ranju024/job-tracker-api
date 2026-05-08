from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewset

router = DefaultRouter() # Instantiates a router that automatically creates URL patterns for your API. 
router.register(r'jobs', JobApplicationViewset, basename='job')

urlpatterns = router.urls