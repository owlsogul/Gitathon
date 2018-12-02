from background_task import background
from logging import getLogger
from teamproject.models import *
from hackathon.models import *
from accounts.models import *
from git_parser.models import *
from pyModule.abuse import *
from collections import Counter


teamCommitList = []
# 1분에 몇 개의 커밋이 , 몇 번 특정한 파일이 수정되면 어뷰징으로 볼 것인지 설정
COMMITCOUNT = 2
FILECOUNT = 2

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
            teamCommit = Commit.objects.filter(teamId = team)
            commitCount = len(teamCommit)
            check=0
            # 만약 teamCommitList에 그 team이 있는지 확인
            for teamCommitInfo in teamCommitList :
                if team.id == teamCommitInfo[0]:
                    if commitCount - teamCommitInfo[1] >= COMMITCOUNT :
                        # 파일 리스트 뽑아서 체크하는 거 필요
                        # 파일 비슷한게 여러번 수정되었음
                        # 어뷰징 스키마 생성
                        checkFileList(hack.id, team.id, teamCommit)

                    teamCommitInfo[1] = commitCount
                    check=1
                    break;

            # teamCommitList에 그 team이 없다
            if check == 0:
                teamCommitList.append([team.id, commitCount])


    print(teamCommitList)


# FileList만들기 -> git show 'commitId' --name-status
def checkFileList(hackName, teamName, teamCommit):

    print("파일리스트체크")

    fileList = []
    nameList = []
    nameCount = []

    # fileList = [ ['commitId', '파일명', '파일명'], ['commitId', '파일명', '파일명'], ~  ]
    for commit in teamCommit :
        fileList.append(makeFileList(hackName, teamName, commit.commitId))

    # nameCount = {'파일이름' : '횟수'}
    nameCount = Counter(sum(fileList, []))

    # count가 FILECOUNT 이상인 것이 존재하면
    # Abusing 스키마 생성
    check = 0
    for value in nameCount.values():
        if value >= FILECOUNT:
            check = 1

    if check == 1:
        team = Team.objects.get(id=teamName)
        for commit in teamCommit:
            abuse = Abusing(teamId=team,context="abusing 의심", commitId=commit.commitId)
            abuse.save()
            print("어뷰징스키마출력")
            print(abuse.commitId)

    print("횟수 출력")
    print(nameCount)




@background(schedule=10)
# Commit 을 주기적으로 감지하기 전 해커톤 참여 팀별로 commit 수 스캔 시작
def setLookCommit():
    # teamCommitList = [ ['teamId', 'commitCount'] ]
    print("start")
    # scanCommit()


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
