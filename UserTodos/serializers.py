from rest_framework import serializers
from .models import TodoTable


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTable
        fields = ['todo_msg', 'is_done']
