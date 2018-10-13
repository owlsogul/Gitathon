from django.urls import path
from . import views

urlpatterns = [
    path('hold/', views.holdHackathon, name='holdHackathon'),
    path('list/', views.listHackathon, name='listHackathon'),
]
