from datetime import datetime
from celery import shared_task

from crontabdb.celery import app
from .models import Scheduler


@app.task
def heart_beat():
    print('Heart Beat! now is ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.task
def every_2mins_beat():
    print('Every 2 minutes Beat! ' + datetime.now().strftime('%H:%M:%S'))
    return 'My Result is: ' + 'Every 2 minutes Beat! ' + datetime.now().strftime('%H:%M:%S')


@shared_task(name="crontabdb.shared_task.execute_scheduler")
def execute_scheduler(scheduler_id):
    print(scheduler_id)
    scheduler = Scheduler.objects.get(pk=scheduler_id)
    print(scheduler_id)
    print(scheduler.title)
    if scheduler.periodic_task.crontab:
        print(scheduler.periodic_task.crontab)
    if scheduler.periodic_task.interval:
        print(scheduler.periodic_task.interval)
