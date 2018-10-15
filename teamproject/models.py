from django.db import models
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    teamName = models.CharField(max_length=100)
    leaderId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)

class TeamContribution(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    comment = models.FloatField()
    code = models.FloatField()
    resource = models.FloatField()

class TeamNotice(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)
    writtenDate = models.DateTimeField('date registered', default=timezone.now())
