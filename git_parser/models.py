from django.db import models
from datetime import *


# Create your models here.

# Abusing 스키마
class Abusing(models.Model):
    teamId = models.ForeignKey('teamproject.Team', on_delete=models.CASCADE)
    context = models.CharField(max_length=200)
    commitId = models.CharField(max_length=200)
