import os
import django

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_crontab_in_database_project.settings')
django.setup()

app = Celery('celeryapp')

app.config_from_object('django.conf:settings')
app.conf.result_expires = int(os.getenv('CELERY_RESULT_EXPIRES'))   # value in seconds
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-my-heart-beat-task-every-single-minute': {
        'task': 'crontabdb.tasks.heart_beat',
        'schedule': crontab(),
    },
    'run-my-15sec-beat-task-every-2mins': {
        'task': 'crontabdb.tasks.every_2mins_beat',
        'schedule': crontab(minute='*/2'),
    },
}
