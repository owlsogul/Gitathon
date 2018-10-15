from django.db import models
from django.utils import timezone

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
    memberId = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)
    #hackId = models.ForeignKey('hackthon', default=None, on_delete=models.CASCADE)
    teamId = models.ForeignKey('teamproject.Team', default=None, on_delete=models.CASCADE)
