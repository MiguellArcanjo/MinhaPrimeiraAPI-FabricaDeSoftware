from rest_framework import serializers
from todo.models import TodoList

class TodoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'