import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillbuddy.settings')
 
app = Celery('skillbuddy')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reminder': {
        'task': 'skillbot.tasks.reminder',
        'schedule': crontab(),  # for testing purposes
    },
    
}





