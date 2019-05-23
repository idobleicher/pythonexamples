from celery import Celery
import time


#The first thing you need is a Celery instance.
# We call this the Celery application or just app for short.
# As this instance is used as the entry-point for everything you want to do in Celery, like creating tasks and managing workers,
# it must be possible for other modules to import it.

param_main ='tasks'
#pyamqp - rabbit amqp
broker_url = 'pyamqp://guest@localhost//'

#The first argument to Celery is the name of the current module.
#This is only needed so that names can be automatically generated when the tasks are defined in the __main__ module.

#The second argument is the broker keyword argument, specifying the URL of
# the message broker you want to use. Here using RabbitMQ (also the default option).

#for RabbitMQ you can use amqp://localhost, or for Redis you can use redis://localhost.

app = Celery(param_main, broker=broker_url)

@app.task
def add(x, y):
    #time.sleep(30)
    return x + y


# if __name__ == '__main__':
#     print("before start ")
#     app.start()
#     print("after start 1")

print("after start in main 2")


print(add(2,2))

async_result = add.delay(2, 2)

#This method is actually a star-argument shortcut to another method called apply_async():
#This is a handy shortcut to the apply_async() method that gives greater control of the task execution (see Calling Tasks):

async_result.ready