from celery import shared_task
from time import sleep

@shared_task(name='subtrection tack')
def sub(x,y):
    sleep(5)
    return x - y