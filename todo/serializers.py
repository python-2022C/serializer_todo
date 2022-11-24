from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Task
        fields = ['name', 'description', 'user']