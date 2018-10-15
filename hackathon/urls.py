from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hold/', views.holdHackathon, name='holdHackathon'),
    path('list/', views.listHackathon, name='listHackathon'),
    url(r'^list/(?P<hackathonInformation_id>\d+)/$', views.applyHackathon),
    url(r'^page/main/(?P<hackathonInformation_id>\d+)/$', views.mainpageHackathon),
]
