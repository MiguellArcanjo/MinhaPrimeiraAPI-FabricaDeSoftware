from rest_framework import serializers
from todo.models import TodoList, Pessoa

class TodoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome']