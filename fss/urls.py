from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListViewSet, TaskDetailViewSet

router = DefaultRouter()
router.register(r'tasks', TaskListViewSet, basename='tasklist')
router.register(r'task', TaskDetailViewSet, basename='taskdetail')

urlpatterns = [
    path('v1/', include(router.urls)),
]

