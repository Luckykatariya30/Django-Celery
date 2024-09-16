from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask,IntervalSchedule
import json


@shared_task(name='subtrection tack')
def sub(x,y):
    sleep(5)
    return x - y

@shared_task
def reminder(id):
    print(f'your session complete: {id}')
    return id



# Create Schedule every 5 seconds

schedule,created = IntervalSchedule.object.get_or_create(
    every=5,
    period = IntervalSchedule.SECONDS,
)
# Schedule the periodic task programmaticlly

PeriodicTask.object.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='myapp.tasks.reminder',
    interval=schedule,
    args=json.dumps(['hello']),
)

