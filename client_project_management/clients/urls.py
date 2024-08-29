# from django.urls import path
# from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsView

# # urlpatterns = [
# #     path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
# #     path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
# #     path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
# #     path('projects/', UserProjectsView.as_view(), name='user-projects'),
# # ]

# # clients/urls.py

# urlpatterns = [
#     path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
#     path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
#     path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
#     path('projects/', UserProjectsView.as_view(), name='user-projects'),
# ]

# clients/urls.py

from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
