from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(TeamContribution)
admin.site.register(TeamNotice)
admin.site.register(TeamChat)
admin.site.register(TeamMergeRequest)
admin.site.register(TeamVote)
admin.site.register(Commit)
admin.site.register(TeamCommitNotification)
