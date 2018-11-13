from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import HttpResponse
from hackathon.forms import *
from hackathon.models import *
from django.contrib import messages
from accounts.models import *
from teamproject.models import *
from django.db.models import Count
from hackathon.viewHackFunction import *
import random

# Create your views here.

# 대회방 개설
def holdHackathon(request):

    form = PostForm()

    if request.method == 'POST':
        # Model Form 을 이용해서 file을 upload할 때 주의
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # form을 DB에 저장
            post = form.save()
            post.hackathonHost = request.session['memberId']
            post.save()
            return redirect('../../lobby/main')

    else:
            form = PostForm()

    return render(request, 'hold.html',{'form':form})

def listHackathon(request):

    contestList = HackathonInformation.objects.all
    q = ''
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    # 제목 검색

    if request.method == 'GET':
        q = request.GET.get('q','')
        if q:
            contestList = HackathonInformation.objects.filter(title__contains=q)

    return render(request, 'listHackathon.html', {'contestList' : contestList, 'q' : q, 'todayDate' : todayDate, 'todayTime' : todayTime})

# 해커톤 목록 페이지에서 신청 버튼을 눌렀을 때
def applyHackathon(request, HackathonInformation_id):

    contestList = HackathonInformation.objects.all
    q = ''
    message = ''
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    # 신청 버튼 클릭
    if request.method == 'POST':
        selection = request.POST['choice']
        appliedContest = HackathonInformation.objects.get(pk = selection)
        userInformation = Member.objects.get(pk=request.session['memberId'])

        # 신청 인원이 초과되지 않은 경우
        if appliedContest.peopleNum > appliedContest.applyNum :

            # 이미 참여한 상태인지 확인 필요(memberID 부분 변경 요망)

            # 이미 참여한 상태라면
            if Participate.objects.filter(memberId = userInformation, hackId = appliedContest) :
                message = '이미 참여한 상태입니다.'
            # 이미 참여한 상태가 아니라면
            else:
                # 해커톤 ID와 참여자 ID 저장 (참여자 ID는 추후 추가)
                temp_participate = Participate(memberId = userInformation, hackId = appliedContest, teamId = None)
                temp_participate.save()
                # applyNum 증가
                appliedContest.applyNum = len(Participate.objects.filter(hackId = appliedContest))
                appliedContest.save()

        # 신청 인원이 초과된 경우
        else :
            message = '신청 인원을 초과하였습니다.'

    return render(request, 'listHackathon.html', {'contestList' : contestList, 'q' : q, 'message' : message, 'todayDate' : todayDate, 'todayTime' : todayTime})

# 해커톤 목록 페이지에서 해커톤 제목을 눌렀을 때
def mainpageHackathon(request, HackathonInformation_id):

    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    return render(request, 'mainpageHackathon.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime})

# 해커톤 팀목록 페이지 눌렀을 때
def teamlistHackathon(request, HackathonInformation_id):


    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time
    # 해커톤 참여 팀과 멤버 쿼리셋
    teamList = Team.objects.filter(participate__hackId = contest).distinct()
    participateList = Participate.objects.filter(hackId = contest)
    # nomemberList = Member.objects.filter(participate__teamId__isnull=True).filter(participate__hackId = contest)
    nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)

    # 자율매칭
    if contest.selectMatching == 0:
        random = ''
    # 랜덤매칭
    else :
        random = 'True'

    # 팀 추가 클릭 시
    if request.method == 'GET':

        contestId = request.GET.get('createTeam')

        if contestId :
            redirect_to = reverse('create', kwargs={'hackId':contest.id})
            return HttpResponseRedirect(redirect_to)


    return render(request, 'teamlistHackathon.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime ,'teamList' : teamList , 'participateList' : participateList, 'nomemberList':nomemberList, 'random' : random})


# 해커톤 팀목록 페이지 팀 참가 신청 시
def applyTeam(request, HackathonInformation_id, Team_id):

    message =''

    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    # 해커톤 참여 팀과 멤버 쿼리셋
    teamList = Team.objects.filter(participate__hackId = contest).distinct()
    team = Team.objects.get(pk = Team_id)
    memberList = Member.objects.filter(participate__teamId = team)
    participateList = Participate.objects.filter(hackId = contest)
    userInformation = Member.objects.get(pk=request.session['memberId'])
    nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)

    # 신청 버튼 클릭
    if request.method == 'POST':

        selection = request.POST['apply']
        appliedTeam = Team.objects.get(pk = selection)
        userInformation = Member.objects.get(pk=request.session['memberId'])

        # 팀 인원이 초과되지 않은 경우
        if contest.memberNum_max > len(memberList) :

            message = len(memberList)

            # 이미 참여한 상태라면
            if memberList.filter(memberId = request.session['memberId']) :
                message = '이미 참여한 상태입니다.'
            # 다른 팀에 참여한 상태라면
            elif participateList.get(memberId = userInformation).teamId :
                message = '이미 다른 팀에 참여했습니다.'
            # 이미 참여한 상태가 아니라면
            else:
                member = participateList.get(memberId = userInformation)
                # 우선은 팀원으로 그냥 추가
                # 수정 요망
                member.teamId = team
                member.save()
                message = '신청이 완료되었습니다.'


        # 팀 인원이 초과된 경우
        else :
            message = '팀 인원이 모두 찼습니다.'

    # 팀 추가 클릭 시
    if request.method == 'GET':

        contestId = request.GET.get('createTeam')

        if contestId :
            redirect_to = reverse('create', kwargs={'hackId':contest.id})
            return HttpResponseRedirect(redirect_to)


    return render(request, 'teamlistHackathon.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime ,'teamList' : teamList , 'participateList' : participateList, 'message' : message, 'nomemberList':nomemberList})


def adminHackathon(request, HackathonInformation_id, Team_id=0):

    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time
    # 해커톤 참여 팀과 멤버 쿼리셋
    teamList = Team.objects.filter(participate__hackId = contest).distinct()
    message = ''

    # 해커톤 관리자만이 접근 가능
    if contest.hackathonHost == request.session['memberId'] :

        # 팀 선택 안했을 때 관리자 메뉴 선택시 -> 팀리스트의 첫번째 팀 보여주기
        if Team_id == 0 :

            # 랜덤 매칭이면 팀이 아직 없어요
            if contest.selectMatching == 1 and len(teamList) == 0:
                team = Team(teamName = "no Team")
                Team_id = team.id
                memberList = None
                nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)
            # 자율 매칭인데 팀이 없어요
            elif contest.selectMatching == 0 and len(teamList) == 0:
                team = Team(teamName = "no Team")
                Team_id = team.id
                memberList = None
                nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)
            else :
                team = teamList.all()[:1].get()
                Team_id = team.id
                memberList = Member.objects.filter(participate__hackId=contest, participate__teamId=team)
                nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)

        # 팀 선택하고 관리자 메뉴 선택시
        else :
            team = teamList.get(pk=Team_id)
            memberList = Member.objects.filter(participate__hackId=contest, participate__teamId=team)
            nomemberList = Member.objects.filter(participate__teamId__isnull=True, participate__hackId = contest)

        if request.method == 'GET':
            nomemberId = request.GET.get('nomemberId')
            randomTeam = request.GET.get('randomTeam')
            resetTeam = request.GET.get('resetTeam')

            # 팀 멤버로 추가
            if nomemberId:
                message = nomemberId
                makeMember = Participate.objects.get(hackId = contest, memberId=nomemberId)
                makeMember.teamId = team
                makeMember.save()
            # 초기화
            if resetTeam:
                randomTeamList = Team.objects.filter(participate__hackId = contest)
                randomTeamList.delete()
                redirect_to = reverse('mainpageHackathon', kwargs={'HackathonInformation_id':contest.id})
                return HttpResponseRedirect(redirect_to)

            # 선택된 팀 멤버 랜덤 매칭
            if randomTeam:
                message = randomTeam
                # 랜덤 매칭 시작
                randomMemberList = Member.objects.filter(participate__hackId=contest)
                # 팀 개수, 총 팀원 수
                max = contest.memberNum_max
                min = contest.memberNum_min
                total = len(randomMemberList)
                rest = 0
                teamNumber = 0;
                memberNumber = 0;

                for i in range(min, max+1) :
                    temp = total % i
                    if temp == 0 :
                        teamNumber = total // i
                        teamNumber+=1
                        memberNumber = i
                        rest = 9999
                    elif rest < temp :
                        rest = temp
                        teamNumber = total // i
                        teamNumber+=1
                        memberNumber = i

                array = []

                for i in range(0, total):
                    array.append(i)

                random.shuffle(array)
                arraySize = len(array)

                for i in range(0, arraySize):

                    if i % memberNumber == 0 :
                        teamIndex = teamNumber - teamNumber + i / memberNumber
                        randomMember = randomMemberList[array[i]]
                        randomTeam = Team(teamName = teamIndex, leaderId = randomMember)
                        randomTeam.save()

                    randomMember = randomMemberList[array[i]]
                    makeMember = Participate.objects.get(hackId = contest, memberId=randomMember)
                    makeMember.teamId = randomTeam
                    makeMember.save()

                redirect_to = reverse('mainpageHackathon', kwargs={'HackathonInformation_id':contest.id})
                return HttpResponseRedirect(redirect_to)


        # 자율매칭
        if contest.selectMatching == 0:
            randomMessage = ''
        # 랜덤매칭
        else :
            randomMessage = 'True'

        return render(request, 'adminHackathon.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime': todayTime, 'teamList' : teamList, 'team' : team, 'message':message, 'memberList':memberList, 'nomemberList':nomemberList, 'random':randomMessage})

    # 해커톤 관리자가 아니라면
    else:
        redirect_to = reverse('mainpageHackathon', kwargs={'HackathonInformation_id':contest.id})
        return HttpResponseRedirect(redirect_to)


# 공지사항 작성 페이지 보여주기
def noticeWriteHack(request, HackathonInformation_id):

    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    # 해커톤 공지사항 작성자
    contestHost = contest.hackathonHost
    W=''
    C=''
    message = ''
    writeMode = 0

    # 해커톤 관리자만이 공지사항 작성 가능
    if contestHost == request.session['memberId'] :

        if request.method == 'POST':

            W = request.POST['write']

            # 작성 버튼을 눌렀을 때
            if W == "작성" :

                writeMode = 0 # 작성모드
                Title = request.POST['Title']
                contents = request.POST['Contents']

                if(Title != "" and contents != ""):

                    hackNotice = HackNotice.objects.create(hackId=contest, title=Title, content=contents)
                    hackNotice.save()
                    redirect_to = reverse('noticeListHack', kwargs={'HackathonInformation_id':contest.id})
                    return HttpResponseRedirect(redirect_to)

                elif(Title == ""):
                    message = '제목을 입력하세요.'
                    return render(request, 'noticeWrite.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'message' : message, 'writeMode' : writeMode})

                else:
                    message = '내용을 입력하세요.'
                    return render(request, 'noticeWrite.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'message' : message, 'writeMode' : writeMode})

            # 취소 버튼을 눌렀을 때
            elif W == "취소" :

                redirect_to = reverse('noticeListHack', kwargs={'HackathonInformation_id':contest.id})
                return HttpResponseRedirect(redirect_to)

            # 공지사항 목록에서 작성 버튼을 눌렀을 때
            elif W == "시작" :
                writeMode = 0
                return render(request, 'noticeWrite.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'message' : message, 'writeMode' : writeMode})

            # 공지사항 글에서 수정 버튼을 눌렀을 때
            elif W == "수정":

                writeMode = 1
                # 오류날거같아
                hackNoticeId = 0

                if request.method == 'POST':

                    hackNoticeId = request.POST['hackNoticeId']

                hackNotice = HackNotice.objects.get(pk=hackNoticeId)

                return render(request, 'noticeWrite.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'message' : message, 'writeMode' : writeMode, 'hackNotice' : hackNotice, 'hackNoticeId' : hackNoticeId})

            # 글을 수정하고 완료를 누를 때
            elif W == "수정완료":

                # 오류날거같아
                hackNoticeId = 0

                if request.method == 'POST':

                    hackNoticeId = request.POST['hackNoticeId']
                    Title = request.POST['Title']
                    Contents = request.POST['Contents']


                hackNotice = HackNotice.objects.get(pk=hackNoticeId)
                hackNotice.title = Title
                hackNotice.content = Contents
                hackNotice.save()

                redirect_to = reverse('noticeListHack', kwargs={'HackathonInformation_id':contest.id})
                return HttpResponseRedirect(redirect_to)


            elif W == "삭제":

                # 오류날거같아
                hackNoticeId = 0

                if request.method == 'POST':
                    hackNoticeId = request.POST['hackNoticeId']

                hackNotice = HackNotice.objects.get(pk=hackNoticeId)
                hackNotice.delete()

                redirect_to = reverse('noticeListHack', kwargs={'HackathonInformation_id':contest.id})
                return HttpResponseRedirect(redirect_to)


        return render(request, 'noticeWrite.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'message' : message})

    # 해커톤 관리자가 아닌경우
    else :

        redirect_to = reverse('noticeListHack', kwargs={'HackathonInformation_id':contest.id})
        return HttpResponseRedirect(redirect_to)




# 작성한 공지사항 목록을 보여주기
def noticeListHack(request, HackathonInformation_id):

    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time
    message = ''

    noticeList = HackNotice.objects.filter(hackId = contest)

    return render(request, 'noticeList.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'noticeList' : noticeList, 'message':message})

# 공지사항 글 하나 보여주기
def noticeViewHack(request, HackathonInformation_id, HackNotice_id):

    # 해커톤 정보
    todayDate = datetime.today().date
    todayTime = datetime.today().time

    hackId = HackathonInformation_id
    hackNoticeId = HackNotice_id
    message = ''

    contest = HackathonInformation.objects.get(pk = hackId)
    contestHost = contest.hackathonHost
    hackNotice = HackNotice.objects.get(pk=hackNoticeId)


    return render(request, 'noticeView.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'contestHost':contestHost, 'hackNotice' : hackNotice, 'message' : message})

# 관리자메뉴 - git 활용도
def gitHackathon(request, HackathonInformation_id, Team_id = 0):

    # 해커톤 정보
    contest = HackathonInformation.objects.get(pk = HackathonInformation_id)
    todayDate = datetime.today().date
    todayTime = datetime.today().time
    selectedTeamId = 0
    message = ''
    gitScore = 0

    # 해커톤 참여 팀 리스트
    teamList = Team.objects.filter(participate__hackId = contest).distinct()

    # 팀 명과 멤버 인원 수
    teamInfo = []

    # 팀아이디

    # 선택된 팀이 없다면
    if Team_id == 0 :
        selectedTeamId = 0
    # 선택된 팀이 있다면
    else :
        selectedTeamId = Team_id


    # 전체 팀들의 raw Data 생성(수정)
    # 전체 팀의 평균  commit수, 수정된 줄 수, merge된 branch 수, 팀원 기여도 점수 가져오기
    # numpy.mean(listName)
    avgTotalData = [600,1500,8,70]
    # 전체 팀의 표준편차
    # numpy.std(listName)
    stdTotalData = [20,18,11,7]

    for team in teamList :

        memberList = Member.objects.filter(participate__hackId = contest, participate__teamId = team)
        # 그 팀들의 raw Data 생성(수정)
        # 한 팀의 commit수, 수정된 줄 수, merge된 branch 수, 팀원 기여도 점수 가져오기
        teamRawData = [500, 1000, 10, 50]

        # 비율이랑 그 팀의 raw Data와 전체 팀들의 raw Data 필요
        gitScore = gitEval(1,1,1,1, avgTotalData, stdTotalData, teamRawData)
        teamInfo.append([team.id, team.teamName, len(memberList), gitScore])

    if request.method == 'POST':

        btnMode = request.POST['gitBtn']

        # 선택된 팀의 깃 활용 점수 보여주기
        if btnMode == '보기' :

            try:
                teamId = request.POST['teamId']
                redirect_to = reverse('gitHackathon', kwargs={'HackathonInformation_id':contest.id, 'Team_id' : teamId})
                return HttpResponseRedirect(redirect_to)

            except:

                redirect_to = reverse('gitHackathon', kwargs={'HackathonInformation_id':contest.id, 'Team_id' : 0})
                return HttpResponseRedirect(redirect_to)

        # 가중치 비율 정해서 평가하기 눌렀을 때
        elif btnMode == '평가' :


            for team in teamInfo :

                try:

                    commitRate = request.POST['Commit']
                    lineRate = request.POST['Line']
                    branchRate = request.POST['Branch']
                    teamRate = request.POST['Team']

                    # 입력 예외 처리
                    if(isNumber(commitRate) == False):
                        raise Exception('commit 수 비율을 올바른 숫자로 다시 입력하세요! ex) 25 or 1 or 3.6')
                    if(isNumber(lineRate) == False):
                        raise Exception('수정된 줄 수 비율을 올바른 숫자로 다시 입력하세요!  ex) 25 or 1 or 3.6')
                    if(isNumber(branchRate) == False):
                        raise Exception('Merge된 branch 수 비율을 올바른 숫자로 다시 입력하세요!  ex) 25 or 1 or 3.6')
                    if(isNumber(teamRate) == False):
                        raise Exception('팀원 기여도 비율을 올바른 숫자로 다시 입력하세요!  ex) 25 or 1 or 3.6')


                    gitScore = gitEval(commitRate, lineRate, branchRate, teamRate, avgTotalData, stdTotalData, teamRawData)

                    team[3] = gitScore

                except Exception as e:
                    message = e


    return render(request, 'gitHackathon.html', {'contest' : contest, 'todayDate' : todayDate, 'todayTime':todayTime, 'message':message, 'teamInfo' : teamInfo, 'selectedTeamId' : selectedTeamId, 'gitScore' : gitScore })
