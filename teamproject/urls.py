from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    url(r'^create/(?P<hackId>\d+)/$', views.createWithHackId, name='create'),
    path('process_create', views.process_create, name='process_create'),
    path('<teamId>/main', views.main, name='main'),
    path('<teamId>/notice', views.notice, name='notice'),
    path('<teamId>/contribution', views.contribution, name='contribution'),
    path('<teamId>/contribution_save', views.contribution_save, name='contribution_save'),
    path('<teamId>/chat', views.chat, name='chat'),
    path('<teamId>/member', views.member, name='member'),
    path('<teamId>/team_notice_post', views.team_notice_post, name='team_notice_post'),
    path('<teamId>/team_notice_view/<noticeId>', views.team_notice_view, name='team_notice_view'),
    path('<teamId>/hack_notice_view/<noticeId>', views.hack_notice_view, name='hack_notice_view'),

    path('<teamId>/merge_request', views.merge_request, name='merge_request'),
    path('<teamId>/vote_agree', views.vote_agree, name='vote_agree'),
    path('<teamId>/vote_disagree', views.vote_disagree, name='vote_disagree'),
    path('<teamId>/merge', views.merge, name='merge'),

]
