import json
from datetime import datetime

from django.http import HttpResponse

from django_celery_beat.models import CrontabSchedule, PeriodicTask, \
        IntervalSchedule, PeriodicTasks

from .models import Scheduler


def createscheduler(request):
    curtime = str(datetime.now())

    # schedule_crontab, _ = CrontabSchedule.objects.get_or_create(
    #     minute="40",
    #     hour="*",
    #     day_of_week="*",
    #     day_of_month="*",
    #     month_of_year="*"
    # )

    schedule_interval, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    periodic_task = PeriodicTask.objects.create(
        # crontab=schedule_crontab,
        interval=schedule_interval,
        name="Periodic task " + curtime,
        task="crontabdb.shared_task.execute_scheduler",
    )

    scheduler = Scheduler.objects.create(
        title="Schedule" + curtime,
        robot=1,
        machines="192.168.1.1, 192.168.1.2, 192.168.1.3",
        config=10,
        periodic_task=periodic_task,
    )
    periodic_task.args=json.dumps((scheduler.id,))
    periodic_task.save()

    print("----hello---")
    return HttpResponse("hello!")


def updatecounters(request):
    # PeriodicTasks.update_changed()
    PeriodicTask.objects.all().update(last_run_at=None)
    for task in PeriodicTask.objects.all():
        PeriodicTasks.changed(task)
    return HttpResponse("counter updated!")
