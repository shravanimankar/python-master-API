# # clients/views.py

# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Client, Project
# from .serializers import ClientSerializer, ProjectSerializer
# from django.utils import timezone

# # class ClientListCreateView(generics.ListCreateAPIView):
# #     queryset = Client.objects.all()
# #     serializer_class = ClientSerializer
# #     permission_classes = [IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(created_by=self.request.user)

# class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'  # Add this line

#     def perform_update(self, serializer):
#         serializer.save(updated_at=timezone.now())

# class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_update(self, serializer):
#         serializer.save(updated_at=timezone.now())

# class ProjectCreateView(generics.CreateAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         client = Client.objects.get(id=self.kwargs['client_id'])
#         serializer.save(client=client, created_by=self.request.user)

# class UserProjectsView(generics.ListAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Project.objects.filter(users=self.request.user)


# clients/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.utils import timezone

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'  # Ensure you have this line if you're using 'id' in your URLs

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(id=self.kwargs['client_id'])
        serializer.save(client=client, created_by=self.request.user)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
