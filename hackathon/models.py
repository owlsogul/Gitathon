from django.db import models
from datetime import *
from time import strftime
from django.utils import timezone
import pygal
from pygal.style import DarkStyle
from django.views.generic import TemplateView

# Create your models here.

# 해커톤 대회 정보
class HackathonInformation(models.Model):

    matching = [(0 , '자율선택'), (1, '랜덤매칭')]
    title = models.CharField(max_length = 100)
    applyDate_start = models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    applyTime_start = models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    applyDate_end = models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    applyTime_end = models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    contestDate_start= models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    contestTime_start= models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    contestDate_end= models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    contestTime_end= models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    applyNum = models.IntegerField(default = 0)
    peopleNum = models.IntegerField()
    memberNum_max = models.IntegerField()
    memberNum_min = models.IntegerField()
    selectMatching = models.IntegerField(choices = matching)
    Images = models.ImageField(upload_to='img')
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now = True)
    hackathonHost = models.CharField(max_length = 100, default = "none")

# 해커톤 공지사항
class HackNotice(models.Model):
    hackNoticeId = models.AutoField(primary_key=True)
    hackId = models.ForeignKey('hackathon.HackathonInformation', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())

# 해커톤 가중치 기반 깃 활용도 평가 비율
class HackUsability(models.Model):
    hackId = models.OneToOneField('hackathon.HackathonInformation', on_delete=models.CASCADE)
    commitRate = models.FloatField(default=25.0)
    lineRate = models.FloatField(default=25.0)
    branchRate = models.FloatField(default=25.0)
    teamRate = models.FloatField(default=25.0)


# 팀별 gitScore점수
class GitScore(models.Model):
    name = models.CharField(max_length=255)
    amt = models.IntegerField()

    def __str__(self):
        return self.name
