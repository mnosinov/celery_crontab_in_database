from django.urls import path

from .views import createscheduler, updatecounters


urlpatterns = [
    path('createscheduler', createscheduler, name='createscheduler'),
    path('updatecounters', updatecounters, name='updatecounters'),
]
