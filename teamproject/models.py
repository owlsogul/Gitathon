from django.db import models
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    teamName = models.CharField(max_length=100)
    leaderId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)

class TeamContribution(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    comment = models.FloatField(default=0.0)
    code = models.FloatField(default=0.0)
    resource = models.FloatField(default=0.0)
    std_score = models.FloatField(default=0.0)

class TeamNotice(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)
    writtenDate = models.DateTimeField('date registered', default=timezone.now())

    def post(self):
        self.writtenDate = timezone.now()
        self.save()

class TeamChat(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    sender = models.ForeignKey('accounts.Member', on_delete=models.SET_NULL, null=True)
    sendedDate = models.DateTimeField('data sended', default=timezone.now())
    chatMsg = models.TextField()

class TeamMergeRequest(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    fromBranch = models.CharField(max_length=100)
    toBranch = models.CharField(max_length=100)

class TeamVote(models.Model):
    requestId = models.ForeignKey('teamproject.TeamMergeRequest', on_delete=models.CASCADE)
    memberId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)
    isAgree = models.BooleanField(default=False)


class Git(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)

class Branch(models.Model):
    branchName = models.CharField(max_length=100)
    containedGit = models.ForeignKey('teamproject.Git', on_delete=models.CASCADE)

class Commit(models.Model):
    containedBranch = models.ForeignKey('teamproject.Branch', on_delete=models.CASCADE)
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    commitId = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100)
    code = models.IntegerField()
    comment = models.IntegerField()
    resource = models.IntegerField()
