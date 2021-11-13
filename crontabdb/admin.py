from django.contrib import admin

from .models import Scheduler


class SchedulerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Scheduler, SchedulerAdmin)
