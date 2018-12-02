from django.urls import path

from git_parser import views

urlpatterns = [
    
    path('v1/tasks/', views.tasks, name='tasks'),

]

