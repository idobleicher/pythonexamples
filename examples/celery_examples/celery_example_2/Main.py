from datetime import timedelta, datetime, timezone

from celery_examples.celery_example_2.tasks import add, add_task_name
from celery_examples.celery_example_2.tasks import myapp2



params = (10 , 2)
async_result = add.apply_async((params))
print(async_result.get( timeout = 10))



#Executes in 5 seconds from now.
# expires after 2 minutes.
async_result = add.apply_async((2, 2), countdown=5 , expires=120)
print(async_result.get( timeout = 20))


#ecutes in 3 seconds from now, specified using eta
utc_now = datetime.now(tz=timezone.utc)
eta =  utc_now+ timedelta(seconds=3)
async_result = add.apply_async((6 ,4), eta= eta)
print(async_result.get( timeout = 30))



#One can also execute a task by name using send_task(), if you don’t have access to the task’s class:

#The name of the registered task are shown when calling
#celery -A celery_examples.celery_example_2.celeryapp2 worker --loglevel=debug

# By default: add_task_name = "celery_examples.celery_example_2.tasks.add"

async_result = myapp2.send_task(add_task_name, [5, 7])
print(async_result.get( timeout = 10))


#the following task will remain in queue
add.apply_async((params))
add.apply_async((params))
add.apply_async((params))