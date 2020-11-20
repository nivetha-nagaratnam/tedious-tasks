from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]