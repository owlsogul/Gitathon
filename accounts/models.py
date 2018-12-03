from django.db import models
from django.utils import timezone
from hackathon.models import *
from teamproject.models import *

# Create your models here.
class Member(models.Model):
    # primary key
    memberId = models.CharField(max_length=20, primary_key=True)
    # field
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=40)
    registerDate = models.DateTimeField('date registered', default=timezone.now())

    def register(self):
        self.registerDate = timezone.now()
        self.save()

class Participate(models.Model):
    memberId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE, null=True)
    hackId = models.ForeignKey('hackathon.HackathonInformation', null=True, on_delete=models.CASCADE)
    teamId = models.ForeignKey('teamproject.Team', null=True, on_delete=models.SET_NULL)
