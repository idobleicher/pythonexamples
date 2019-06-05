from celery import Celery
from celery.signals import worker_ready, worker_shutdown, worker_shutting_down
import logging


#TO run:
#~/projects/personal/pythonexamples/examples$ celery -A celery_examples.celery_example_1.celeryapp1 worker --loglevel=debug


log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("celeryapp_2")
logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler('celery_app_2.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(log_format)

logger.addHandler(f_handler)

#The first thing you need is a Celery instance.
# We call this the Celery application or just app for short.
# As this instance is used as the entry-point for everything you want to do in Celery, like creating tasks and managing workers,
# it must be possible for other modules to import it.


param_main ='tasks'

#pyamqp - rabbit amqp
broker_url = 'pyamqp://guest@localhost//'
backend = 'amqp://'

include_modules= [ 'celery_examples.celery_example_2.tasks']

#The first argument to Celery is the name of the current module.
#This is only needed so that names can be automatically generated when the tasks are defined in the __main__ module.

#The second argument is the broker keyword argument, specifying the URL of
# the message broker you want to use. Here using RabbitMQ (also the default option).

#for RabbitMQ you can use amqp://localhost, or for Redis you can use redis://localhost.
myapp2 = Celery(param_main, broker=broker_url ,backend= backend, include = include_modules)


@worker_ready.connect
def at_start(sender, **k):
    logger.debug("in at start")
    print("in at start")
    with sender.app.connection() as conn:
        pass
    # sender.app.send_task('app.modules.task', args, connection=conn, ...)


@worker_shutdown.connect
def on_worker_shutdown(*a, **kw):
    logger.debug('worker shut down')
    print("worker shut down")




@worker_shutting_down.connect
def worker_shutting_down(*a, **kw):
    logger.debug('worker begins shut down sig %s how %s exitcode %s',
                  kw['sig'], kw['how'], kw['exitcode'])
    print("in worker_shutting_down")




# if __name__ == '__main__':
#     print("before start ")
#     myapp2.start()
#     print("after start 1")
