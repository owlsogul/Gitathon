from django.shortcuts import render
from teamproject.models import *
from accounts.models import *

import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger

from .tasks import test, lookCommit, setLookCommit

logger = getLogger(__name__)

@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        return _post_tasks(request)
    else:
        return JsonResponse({}, status=405)

def _post_tasks(request):
    message = request.POST['message']
    logger.debug('calling demo_task. message={0}'.format(message))
    test(message, repeat = 20)
    return JsonResponse({}, status=302)


## abusing ##
@csrf_exempt
def startTasks(request):
    if request.method == 'POST':
        return catchAbusing(request)
    else:
        return JsonResponse({}, status=405)


def catchAbusing(request):
    message = request.POST['message']
    setLookCommit()
    lookCommit(message, repeat=30)
    return JsonResponse({}, status=302)

# Create your views here.
@csrf_exempt
def get_commit_with_member(request):
    if request.method == 'POST':
        memberId = request.POST['memberId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__memberId = memberId, teamName=teamName).distinct()
        commits = Commit.objects.filter(teamId=team[0])

        commitIdArr = []
        commitIdArrDic = {}
        for commit in commits:
            commitIdArr.append(commit.commitId)
        commitIdArrDic['commits'] = commitIdArr
        return JsonResponse(commitIdArrDic)

@csrf_exempt
def get_commit_with_hack(request):
    if request.method == 'POST':
        hackId = request.POST['hackId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__hackId = hackId, teamName=teamName).distinct()
        commits = Commit.objects.filter(teamId=team[0])

        commitIdArr = []
        commitIdArrDic = {}
        for commit in commits:
            commitIdArr.append(commit.commitId)
        commitIdArrDic['commits'] = commitIdArr
        return JsonResponse(commitIdArrDic)

@csrf_exempt
def add_commit_with_member(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.POST['data'])
        memberId = request.POST['memberId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__memberId = memberId, teamName=teamName).distinct()

        branchList = received_json_data['branchList']
        branchData = received_json_data['branchData']
        numCommit = 0
        for branchName in branchList:
            for commitData in branchData[branchName]:
                commit = Commit.objects.create(commitId=commitData['commit'], teamId=team[0], author=commitData['author'], comment=commitData['comment'], code=commitData['code'], resource=commitData['resource'])
                commit.save()
                numCommit += 1

        if numCommit > 0:
            teamCommitNoti = TeamCommitNotification.objects.create(teamId=team)
            teamCommitNoti.sendNotification()
        return JsonResponse(received_json_data)


@csrf_exempt
def add_commit_with_hack(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.POST['data'])
        hackId = request.POST['hackId']
        teamName = request.POST['teamName']

        team = Team.objects.filter(participate__hackId = hackId, teamName=teamName).distinct()

        branchList = received_json_data['branchList']
        branchData = received_json_data['branchData']
        numCommit = 0
        for branchName in branchList:
            for commitData in branchData[branchName]:
                commit = Commit.objects.create(commitId=commitData['commit'], teamId=team[0], author=commitData['author'], comment=commitData['comment'], code=commitData['code'], resource=commitData['resource'])
                commit.save()
                numCommit += 1

        if numCommit > 0:
            teamCommitNoti = TeamCommitNotification.objects.create(teamId=team)
            teamCommitNoti.sendNotification()

        return JsonResponse(received_json_data)
