from rest_framework import routers
router = routers.DefaultRouter()

from api.views import BlogViewSet

router.register(r'blog', BlogViewSet)

urlpatterns = router.urls
