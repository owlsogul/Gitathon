from django.urls import path

from git_parser import views

urlpatterns = [

    path('v1/tasks/', views.tasks, name='tasks'),
    path('abusing/', views.startTasks, name='startTasks'),
    
    path('get_commit_with_hack', views.get_commit_with_hack, name='get_commit_with_hack'),
    path('get_commit_with_member', views.get_commit_with_member, name='get_commit_with_member'),

]
