from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name='main'),
    url('join', views.join, name='join'),
]
