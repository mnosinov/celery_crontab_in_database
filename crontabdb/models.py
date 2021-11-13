from django.db import models
from django_celery_beat.models import PeriodicTask


class Scheduler(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    periodic_task = models.OneToOneField(
        PeriodicTask, on_delete=models.CASCADE, null=False, blank=False
    )
    robot = models.IntegerField()
    machines = models.CharField(max_length=40)
    config = models.IntegerField()
