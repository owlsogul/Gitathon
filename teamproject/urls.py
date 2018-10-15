from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create_process', views.create, name='create'),
    path('<teamId>/main', views.main, name='main'),
]
