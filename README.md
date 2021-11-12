# celery_crontab_in_database_project - django, celelry, redis and crontasks in database sample project

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

test application and watch results in admin panel
------------------
see corresponding sh scripts
