from django.forms import ModelForm
from hackathon.models import *

class Form(ModelForm):
    class Meta:
        model = hackathonInformation
        # fields = '__all__'
        # exclude = ['title']
        fields = ('title', 'applyDate_start', 'applyTime_start', 'applyDate_end', 'applyTime_end', 'peopleNum', 'memberNum_max', 'memberNum_min', 'selectMatching', 'Images', 'text',)
