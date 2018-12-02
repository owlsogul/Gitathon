from background_task import background
from logging import getLogger
from teamproject.models import *
from hackathon.models import *
from accounts.models import *

teamCommitList = []

@background(schedule=60)
def test(message):
    print(message)

# 1분마다
# 해커톤 참여 팀별로 commit을 검사하면서
# 이전 commit 수보다 2이상 증가하면 Abusing 스키마 생성
@background(schedule=60)
def lookCommit(message):

    allHack = HackathonInformation.objects.all().order_by('id')

    for hack in allHack :
        print(hack.title)
        teamInHack = Team.objects.filter(participate__hackId = hack).distinct().order_by('id')

        for team in teamInHack :
            # 만약 teamCommitList에 그 team이 있는지 확인
            teamCommit = Commit.objects.filter(teamId = team)
            commitCount = len(teamCommit)
            for teamCommitInfo in teamCommitList :
                if team.id == teamCommitInfo[0]:
                    if commitCount - teamCommitInfo[1] >= 2 :
                        print("어뷰징 발생")
                    teamCommitInfo[1] = commitCount
                else :
                    teamCommitList.append([team.id, commitCount])


    print(teamCommitList)



@background(schedule=10)
# Commit 을 주기적으로 감지하기 전 해커톤 참여 팀별로 commit 수 스캔 시작
def setLookCommit():
    # teamCommitList = [ ['teamId', 'commitCount'] ]
    print("start")
    scanCommit()


def scanCommit():

    allHack = HackathonInformation.objects.all().order_by('id')

    for hack in allHack :
        print("scan Commit")
        teamInHack = Team.objects.filter(participate__hackId = hack).distinct().order_by('id')

        for team in teamInHack :

            teamCommit = Commit.objects.filter(teamId = team)
            teamCommitList.append([team.id, len(teamCommit)])


    print("scan결과")
    print(teamCommitList)
