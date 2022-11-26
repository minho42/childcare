from celery import Celery
from celery.schedules import crontab

from project.celery import app

from .updater import Updater


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(crontab(hour="*/1"), update.s(), name="")
    sender.add_periodic_task(crontab(minute="*/30"), update.s(), name="")


@app.task
def update():
    up = Updater()
    up.update()
