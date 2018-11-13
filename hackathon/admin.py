from django.contrib import admin
from .models import HackathonInformation
from .models import HackNotice

# Register your models here.
admin.site.register(HackathonInformation)
admin.site.register(HackNotice)
