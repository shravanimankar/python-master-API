# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from django.contrib.auth.models import User
# from .models import Client, Project
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Client

class ClientAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')
        self.client_data = {'client_name': 'TestClient'}

    def test_create_client(self):
        response = self.client.post(reverse('client-list-create'), self.client_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['client_name'], 'TestClient')

    def test_get_clients(self):
        Client.objects.create(client_name='TestClient', created_by=self.user)
        response = self.client.get(reverse('client-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_update_client(self):
        client_obj = Client.objects.create(client_name='TestClient', created_by=self.user)
        updated_data = {'client_name': 'UpdatedClient'}
        response = self.client.put(reverse('client-detail', args=[client_obj.id]), updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['client_name'], 'UpdatedClient')

    def test_delete_client(self):
        client_obj = Client.objects.create(client_name='TestClient', created_by=self.user)
        response = self.client.delete(reverse('client-detail', args=[client_obj.id]))
        self.assertEqual(response.status_code, 204)

# class ProjectAPITest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='password')
#         self.client_user = User.objects.create_user(username='clientuser', password='password')
#         self.client = APIClient()
#         self.client.login(username='testuser', password='password')
#         self.client_obj = Client.objects.create(client_name='TestClient', created_by=self.user)
#         self.project_data = {'project_name': 'TestProject', 'users': [self.client_user.id]}

#     def test_create_project(self):
#         response = self.client.post(reverse('project-create', args=[self.client_obj.id]), self.project_data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data['project_name'], 'TestProject')
class ProjectAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client_user = User.objects.create_user(username='clientuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')
        self.client_obj = Client.objects.create(client_name='TestClient', created_by=self.user)
        self.project_data = {'project_name': 'TestProject', 'users': [self.client_user.id]}

    def test_create_project(self):
        response = self.client.post(reverse('project-create', args=[self.client_obj.id]), self.project_data)
        print("Response Data:", response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, 201)

    # def test_get_user_projects(self):
    #     project_obj = Project.objects.create(project_name='TestProject', client=self.client_obj, created_by=self.user)
    #     project_obj.users.add(self.client_user)
    #     self.client.login(username='clientuser', password='password')
    #     response = self.client.get(reverse('user-projects'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertGreater(len(response.data), 0)
