from celery import Celery



#TO run:
#~/projects/personal/pythonexamples/examples$ celery -A celery_examples.celery_example_1.celeryapp1 worker --loglevel=debug


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

# if __name__ == '__main__':
#     print("before start ")
#     app.start()
#     print("after start 1")
