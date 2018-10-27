from django.contrib import admin
from .models import HackathonInformation
from .models import Participate
from .models import tempLoginInformation

# Register your models here.
admin.site.register(HackathonInformation)
admin.site.register(Participate)
admin.site.register(tempLoginInformation)
