from django.contrib import admin
from django.db import models
from main.models import League, Team, Run, Period, Schedule, Schedule_line_item

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Run)
admin.site.register(Period)
admin.site.register(Schedule)
admin.site.register(Schedule_line_item)







