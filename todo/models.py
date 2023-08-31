from django.db import models

# Create your models here.

class TodoList(models.Model):
    tarefa = models.CharField(max_length=50)

    choices_status = [
        ('Pronto', 'Pronto'),
        ('Em andamento', 'Em Andamento'),
        ('Pendente', 'Pendente'),
    ]

    status = models.CharField(choices=choices_status, max_length=12)
