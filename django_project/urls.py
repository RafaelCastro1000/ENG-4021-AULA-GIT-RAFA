
from django.contrib import admin
from django.urls import path
from appdoluis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('tasks/', views.list_tasks, name="tasks-list"),
    path('tasks/create/', views.create_task),
    path('tasks/edit/<task_id>', views.update_task),
    path('tasks/delete/<task_id>', views.delete_task),
]
