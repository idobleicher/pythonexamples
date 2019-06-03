from __future__ import absolute_import, unicode_literals
from celery import Celery

tasks_queue = "my_tasks_queue"

app = Celery('celery_app_todo',
             broker='amqp://',
             backend='amqp://',
             include=['celery_app_todo.tasks'])
# STARTED state is not enabled by default so we flip it on
app.conf.update(task_track_started=True)



# Optional configuration, see the application user guide.
app.conf.update (
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
