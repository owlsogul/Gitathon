from django.views import View
from django.shortcuts import redirect, render
from .models import Member
from django.db.models import Q
# Create your views here.
class Login(View):

    def get(self, request, *args, **kwargs):
        return redirect('../lobby/')

    def post(self, request, *args, **kwargs):
        gotMemberId = request.POST['memberId']
        gotPassword = request.POST['password']
        if Member.objects.filter(memberId = gotMemberId, password = gotPassword).count() == 1:
            request.session['memberId'] = gotMemberId
        return redirect('../lobby/')

class Logout(View):

    def get(self, request, *args, **kwargs):
        del request.session['memberId']
        return redirect('../lobby/')

    def post(self, request, *args, **kwargs):
        del request.session['memberId']
        return redirect('../lobby/')

class Register(View):

    def get(self, request, *args, **kwargs):
        return redirect('../lobby/')

    def post(self, request, *args, **kwargs):
        gotMemberId = request.POST['memberId']
        gotEmail = request.POST['email']
        gotPassword = request.POST['password']
        if Member.objects.filter(Q(memberId = gotMemberId) | Q(email=gotEmail)).count() == 1:
            print('Already exist account')
        else:
            member = Member.objects.create(memberId=gotMemberId, email=gotEmail, password=gotPassword)
            member.register();
            print('Register!')
        return redirect('../lobby/')
