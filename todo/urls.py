from rest_framework import routers
from todo.views import TodoListViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoListViewSet)
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls