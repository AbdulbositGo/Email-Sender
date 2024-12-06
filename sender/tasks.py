from time import sleep
from celery import shared_task


@shared_task(bind=True)
def sleepy(self, seconds=10):
    sleep(seconds)
    return "Done"