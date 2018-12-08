from django.urls import path

from git_parser import views

urlpatterns = [

    path('v1/tasks/', views.tasks, name='tasks'),
    path('abusing/', views.startTasks, name='startTasks'),

    path('get_commit_with_hack', views.get_commit_with_hack, name='get_commit_with_hack'),
    path('get_commit_with_member', views.get_commit_with_member, name='get_commit_with_member'),
    
    path('add_commit_with_hack', views.add_commit_with_hack, name='add_commit_with_hack'),
    path('add_commit_with_member', views.add_commit_with_member, name='add_commit_with_member'),

]
