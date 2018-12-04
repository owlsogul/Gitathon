from django.shortcuts import render
from django.http import JsonResponse

from teamproject.models import *
from accounts.models import *

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

    received_json_data = json.loads(request.POST['data'].decode("utf-8"))
    memberId = request.POST['memberId']
    teamName = request.POST['teamName']

    team = Team.objects.filter(participate__memberId = memberId, teamName=teamName).distinct()
    git = Git.objects.get(teamId=team)

    branchList = received_json_data['branchList']
    branchData = received_json_data['branchData']
    for branchName in branchList:
        branch = Branch.objects.filter(commit_teamId = team.pk(), branchName=branchName).distinct()
        if branch is None:
            branch = Branch.objects.create(branchName=branchName)
            branch.save()
        for commitData in brachData['branchName']:
            commit = Commit.objects.create(containedGit = git, author=commitData['author'], comment=commitData['comment'], code=commitData['code'], resource=commitData['resource'], branchId=branch)
            commit.save()



    return JsonResponse(received_json_data)
