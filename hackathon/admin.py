from django.contrib import admin
from .models import hackathonInformation
from .models import participate
from .models import tempLoginInformation

# Register your models here.
admin.site.register(hackathonInformation)
admin.site.register(participate)
admin.site.register(tempLoginInformation)
