from rest_framework import viewsets
from todo.models import TodoList
from todo.serializers import TodoListSerializers

# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers
