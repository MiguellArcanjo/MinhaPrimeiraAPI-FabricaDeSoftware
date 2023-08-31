from rest_framework import viewsets
from todo.models import TodoList, Pessoa
from todo.serializers import TodoListSerializers, PessoaSerializer

# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer