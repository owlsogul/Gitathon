from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create/<hackId>', views.createWithHackId, name='createWithHackId'),
    path('process_create', views.process_create, name='process_create'),
    path('<teamId>/main', views.main, name='main'),
    path('<teamId>/notice', views.notice, name='notice'),
    path('<teamId>/contribution', views.contribution, name='contribution'),
    path('<teamId>/chat', views.chat, name='chat'),
    path('<teamId>/member', views.member, name='member'),
]
