from django.urls import path, include
from djangoProject1.views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:id>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
]
