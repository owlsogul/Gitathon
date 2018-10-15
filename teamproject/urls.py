from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('process_create', views.process_create, name='process_create'),
    path('<teamId>/main', views.main, name='main'),
]
