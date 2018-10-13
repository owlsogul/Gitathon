from django.shortcuts import render
from django.http import HttpResponse
from hackathon.forms import *
from hackathon.models import *

# Create your views here.

# 대회방 개설
def holdHackathon(request):
    form = Form()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # form을 DB에 저장
            form.save()
    else:
            form = Form()

    return render(request, 'hold.html',{'form':form})

def listHackathon(request):
    contestList = hackathonInformation.objects.all
    return render(request, 'listHackathon.html', {'contestList' : contestList})
