from celery import Celery
from celery_examples.celery_example_1.app_1_celery_config import CeleryConfig
import time


#TO run:
#~/projects/personal/pythonexamples/examples$ celery -A celery_examples.celery_example_1.celeryapp1 worker --loglevel=debug

#T he application is thread-safe so that multiple Celery applications with different configurations,
# components, and tasks can co-exist in the same process space.


# Name of the main module if running as `__main__`.
#This is used as the prefix for auto-generated task names.
main_module_name= "celery_example_1"

#broker (str): URL of the default broker used.
broker = 'redis://localhost'

#The backend argument specifies the result backend to use,
# #The result store backend class, or the name of the backend  class to use.
result_backend = 'redis://localhost'


#  include (List[str]): List of modules every worker should import.
include_modules= [ 'celery_examples.celery_example_1.celeryapp1' ,'celery_examples.celery_example_1.tasks']

add_queue_name = "add_queue_1"

# Laziness - Creating a Celery instance will only do the following:
#
# 1.Create a logical clock instance, used for events.
# 2.Create the task registry.
# 3.Set itself as the current app (but not if the set_as_current argument was disabled)
# 4.Call the app.on_init() callback (does nothing by default).

myapp = Celery(main_module_name ,
             broker=broker,
              backend=result_backend,
             include=include_modules)


#you can  set configuration values directly:
#myapp.conf.timezone = 'Europe/London'
#print(myapp.conf.timezone)


#or from configuration object
celleryConfig = CeleryConfig()
myapp.config_from_object(celleryConfig )
print(myapp.conf.timezone)


# Optional configuration, see the application user guide.
myapp.conf.update(  result_expires=360000)


#this is how you’d route a misbehaving task to a dedicated queue:
#it's not a must
#note - the tasks @myapp.task decorator should have a name

myapp.conf.update(task_routes={
   'celery_examples.celery_example_1.tasks.add': {'queue': add_queue_name},
   }
)


print(myapp.conf.result_expires)

@myapp.task(bind=True)
def add1(self , x, y):
    time.sleep(2)
    return x + y

# asyncres = add.apply_async((1, 1), queue=add_queue_name)
# print(asyncres.backend)
#
#
# actual_result=asyncres.get(timeout=5 )





