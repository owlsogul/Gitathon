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
            commit = Commit.objects.create(containedGit = git, author=commitData['author'], comment=commitData['comment'], code=commitData['code'], resource=commitData['resource'])



    return JsonResponse(received_json_data)
