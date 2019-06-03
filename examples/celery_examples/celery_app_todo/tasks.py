from __future__ import absolute_import, unicode_literals
from .celery import app , tasks_queue
import logging
import time


logging.basicConfig(filename='celery_app_todo.log',level=logging.DEBUG)
logging.warning('Watch out!')

@app.task(bind=True)
def add(self , x, y):
    time.sleep(3)
    return x + y


@app.task(bind=True)
def mul(self , x, y):
    time.sleep(3)
    return x * y




asyn_result1=add.apply_async((2, 2)  )
#asyn_result1=add.apply_async((2, 2) ,  queue=tasks_queue )
#In the above example the task will be sent to a queue named lopri and the task will execute, at the earliest, 30 seconds after the message was sent.
asyn_result2=add.apply_async((2, 2), queue=tasks_queue, countdown=30)

logging.info(asyn_result1.ready())
logging.info(asyn_result2.ready())

timeout = 300   # [seconds]
timeout_start = time.time()

# Busy Waiting With Sleep
while time.time() < timeout_start + timeout:
    logging.info(time.time())

    logging.info("res 1 id:" + asyn_result1.id)
    logging.info("res 1 ready:" + str(asyn_result1.ready()))
    logging.info("res 1 status:" + str(asyn_result1.status))
    logging.info("res 1 state:" + str(asyn_result1.state))
    logging.info("res 1 backend:" + str(asyn_result1.backend))

    logging.info("res 2 id:" + asyn_result2.id)
    logging.info("res 2 status:" + str(asyn_result2.status))
    logging.info("res 2 ready:" + str(asyn_result2.ready()))
    logging.info("res 2 state:" + str(asyn_result2.state))
    logging.info("res 2 backend:" + str(asyn_result2.backend))
    time.sleep(20)
