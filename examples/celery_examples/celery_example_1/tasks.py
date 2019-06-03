from __future__ import absolute_import, unicode_literals
from celery_examples.celery_example_1.celeryapp1 import myapp
import logging
import time

logging.basicConfig(level=logging.DEBUG,filename='celeryapp1.log')

#When you send a task message in Celery, that message won’t contain any source code,
# but only the name of the task you want to execute.

# This works similarly to how host names work on the internet:
# every worker maintains a mapping of task names to their actual functions, called the task registry.

#Whenever you define a task, that task will also be added to the local registry:

#LAziness - The app.task() decorators don’t create the tasks at the point when the task is defined,
# instead it’ll defer the creation of the task to happen either when the task is used,
# or after the application has been finalized,

@myapp.task(bind=True , name = "add")
def add(self , x, y):
    logging.debug("in add")
    time.sleep(2)
    logging.debug(self.request.id)
    return x + y


@myapp.task
def mul(x, y):
    return x * y


@myapp.task
def xsum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    print(add.name)
    print(add.__evaluated__())
    add(1 ,2)
    print(add.__evaluated__())
    xsum([1 ,2])

    #celery_example_1.add
