import os
from time import sleep
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

@app.task(name='addition task')
def add(x,y):
    sleep(5)
    return x+y


## seconde method

app.conf.beat_schedule = {
    'every_one_mintes':{
        'task':'myapp.tasks.sub',
        'schedule':10,
        'args':(22,12),
    }
}

# Used to timedelta 

# app.conf.beat_schedule = {
#     'every_one_mintes':{
#         'task':'myapp.tasks.sub',
#         'schedule':timedelta(secondes=10)
#         'args':(22,12),
#     }
# }

# Used to crontab 

# app.conf.beat_schedule = {
#     'every_one_mintes':{
#         'task':'myapp.tasks.sub',
#         'schedule':crontab(mintes='*/1'),
#         'args':(22,12),
#     }
# }

# Execute every monday morning at 7.30am
#schedule : crontab(hour=7,minte=30 , day-of-week=1)