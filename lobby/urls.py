from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name='main'),
    url('join', views.join, name='join'),
]
