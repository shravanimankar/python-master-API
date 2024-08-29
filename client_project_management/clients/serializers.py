from rest_framework import serializers
from .models import Client, Project

# class ProjectSerializer(serializers.ModelSerializer):
#     users = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Project
#         fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']
