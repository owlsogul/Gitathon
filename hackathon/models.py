from django.db import models
from datetime import *

# Create your models here.

# 해커톤 대회 정보
class hackathonInformation(models.Model):

    matching = [(0 , '자율선택'), (1, '랜덤매칭')]
    title = models.CharField(max_length = 100)
    applyDate_start = models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    applyTime_start = models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    applyDate_end = models.DateField(help_text="Please use the following format : <em>YYYY-MM-DD</em>")
    applyTime_end = models.TimeField(help_text="Please use the following format : <em>12:00:00</em>")
    applyNum = models.IntegerField(default = 0)
    peopleNum = models.IntegerField()
    memberNum_max = models.IntegerField()
    memberNum_min = models.IntegerField()
    selectMatching = models.IntegerField(choices = matching)
    Images = models.FileField(blank=True, upload_to='./hackathon/static/uploads')
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now = True)
    # 회원정보 아직 없어서 default로 wkdthf21
    hackathonHost = models.CharField(max_length = 100, default = "wkdthf21")

class participate(models.Model):
    # 회원정보 아직 없어서 default로 wkdthf21
    memberID = models.CharField(max_length = 100, default = "wkdthf21")
    # participate의 hackathonID는 hackathonInformation ID를 참조
    # 해커톤 대회 정보가 지워지면 자동으로 participate의 정보도 지워진다.
    hackathonID = models.ForeignKey(hackathonInformation, on_delete=models.CASCADE)
