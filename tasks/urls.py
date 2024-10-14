# tasks/urls.py
from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    task_list,
    task_create,
    task_update,
    task_delete,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/update/<int:pk>/', task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', task_delete, name='task_delete'),
]
