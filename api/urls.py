from rest_framework.routers import DefaultRouter

from api.views import TodoViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet, base_name='todo')

urlpatterns = router.urls
