# before running celery beat - celery worker must be already running - sh run_celery_worker.sh
# celery -A crontabdb beat -l debug	# just for schedules in code
celery -A crontabdb beat -l debug -S django	# for schedules from database and from code
