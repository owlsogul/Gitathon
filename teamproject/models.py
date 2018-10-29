from django.db import models
from django.utils import timezone

# Create your models here.

class Team(models.Model):

    teamName = models.CharField(max_length=100)
    leaderId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)
