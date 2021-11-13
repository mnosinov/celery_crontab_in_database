# celery_crontab_in_database_project - django, celelry, redis: interval and crontab schedules in database sample project

.env content:
---
SECRET_KEY=

ALLOWED_HOSTS_LIST=localhost, 127.0.0.1

DEBUG_MODE=True

CELERY_RESULT_EXPIRES=120		(2 minutes)

# How to run
1. django runserver (in vitualenv)
2. redis-server
3. run celery worker (in vitualenv)
4. run celery beat (in vitualenv)
5. use views to test different scenarios and watch console of celery beat and celery worker

test application and watch results in admin panel
------------------
* ```http://127.0.0.1:8020/createscheduler```   -- creates sample schedule for IntervalSchedule or CrontabSchedule - uncomment what you need.
* ```http://127.0.0.1:8020/updatecounters```	-- reset counters - see documentation https://github.com/celery/django-celery-beat
