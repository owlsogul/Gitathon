from django.shortcuts import render
from django.http import HttpResponse
from hackathon.forms import *
from hackathon.models import *
from django.contrib import messages

# Create your views here.

# 대회방 개설
def holdHackathon(request):
    form = Form()

    if request.method == 'POST':
        # Model Form 을 이용해서 file을 upload할 때 주의
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            # form을 DB에 저장
            form.save()
    else:
            form = Form()

    return render(request, 'hold.html',{'form':form})

def listHackathon(request):

    contestList = hackathonInformation.objects.all
    q = ''

    # 제목 검색

    if request.method == 'GET':
        q = request.GET.get('q','')
        if q:
            contestList = hackathonInformation.objects.filter(title__contains=q)

    return render(request, 'listHackathon.html', {'contestList' : contestList, 'q' : q})


def applyHackathon(request, hackathonInformation_id):

    # 임의의 유저 ID
    USERID = 'yedoriii6'
    contestList = hackathonInformation.objects.all
    q = ''
    message = ''

    # 신청 버튼 클릭
    if request.method == 'POST':
        selection = request.POST['choice']
        appliedContest = hackathonInformation.objects.get(pk = selection)

        # 신청 인원이 초과되지 않은 경우
        if appliedContest.peopleNum > appliedContest.applyNum :

            # 이미 참여한 상태인지 확인 필요(memberID 부분 변경 요망)

            # 이미 참여한 상태라면
            if participate.objects.filter(memberID = USERID, hackathonID = appliedContest) :
                message = '이미 참여한 상태입니다.'
            # 이미 참여한 상태가 아니라면
            else:
                # 해커톤 ID와 참여자 ID 저장 (참여자 ID는 추후 추가)
                temp_participate = participate(memberID = USERID , hackathonID = appliedContest)
                temp_participate.save()
                # applyNum 증가
                appliedContest.applyNum += 1
                appliedContest.save()

        # 신청 인원이 초과된 경우
        else :
            message = '신청 인원을 초과하였습니다.'

    return render(request, 'listHackathon.html', {'contestList' : contestList, 'q' : q, 'message' : message})
