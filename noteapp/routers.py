from rest_framework.routers import DefaultRouter

from userapp.viewsets import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls
