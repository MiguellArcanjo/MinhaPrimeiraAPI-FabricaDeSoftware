from rest_framework import routers
from todo.views import TodoListViewSet

router = routers.DefaultRouter()
router.register(r'', TodoListViewSet)
urlpatterns = router.urls