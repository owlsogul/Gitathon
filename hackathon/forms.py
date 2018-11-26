from django.forms import *
from hackathon.models import *
from django import forms

class PostForm(ModelForm, forms.Form):

    class Meta:
        model = HackathonInformation
        # fields = '__all__'
        # exclude = ['title']
        fields = ['title', 'applyDate_start', 'applyTime_start', 'applyDate_end', 'applyTime_end', 'contestDate_start', 'contestTime_start', 'contestDate_end', 'contestTime_end' , 'peopleNum', 'memberNum_max', 'memberNum_min', 'selectMatching', 'Images', 'text', 'hackathonHost']
        widgets = {'hackathonHost': forms.HiddenInput()}
