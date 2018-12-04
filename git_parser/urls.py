from django.urls import path
from . import views

urlpatterns = [
    path('get_commit_with_hack', views.get_commit_with_hack, name='get_commit_with_hack'),
    path('get_commit_with_member', views.get_commit_with_member, name='get_commit_with_member'),
]
