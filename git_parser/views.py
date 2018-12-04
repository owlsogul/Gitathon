from django.shortcuts import render
from django.http import JsonResponse

from teamproject.models import *
from accounts.models import *

# Create your views here.
def get_commit_with_member(request):
    if request.method == 'POST':
        memberId = request.POST['memberId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__memberId = memberId, teamName=teamName).distinct()
        commits = Commit.objects.filter(teamId=team)

        commitIdArr = []
        commitIdArrDic = {}
        for commit in commits:
            commitIdArr.append(commit.commitId)
        commitIdArrDic['commits'] = commitIdArr
        return JsonResponse(commitIdArrDic)

def get_commit_with_hack(request):
    if request.method == 'POST':
        hackId = request.POST['hackId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__hackId = hackId, teamName=teamName).distinct()
        commits = Commit.objects.filter(teamId=team)

        commitIdArr = []
        commitIdArrDic = {}
        for commit in commits:
            commitIdArr.append(commit.commitId)
        commitIdArrDic['commits'] = commitIdArr
        return JsonResponse(commitIdArrDic)

def add_commit_with_member(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    return JsonResponse(received_json_data)
