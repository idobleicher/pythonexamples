from celery_examples.celery_example_1.celeryapp1 import myapp , add_queue_name
from celery_examples.celery_example_1.tasks import mul, add , xsum
from celery_examples.celery_example_1.celeryapp1 import add1
from celery_examples.celery_example_1.DumpCam import DumpCam
from celery.events import EventReceiver



# def main(app, freq=2.0):
#     state = app.events.State()
#     with myapp.connection() as connection:
#         recv = app.events.Receiver(connection, handlers={'*': state.event})
#         with DumpCam(state, freq=freq):
#             recv.capture(limit=None, timeout=None)
#
# if __name__ == '__main__':
#     main(myapp)


s = myapp.connection()


def run_task_async(task_function , args, timeout = None ) :
   # asyncres = add.delay(args)
   print('Tasks: {0} params {1}'.format(task_function.__name__ , args))
   async_result = task_function.apply_async((args))

   print("Ready: {0}".format(async_result.ready()))
   actual_result = async_result.get(timeout=timeout)
   print("Ready: {0}".format(async_result.ready()))
   print("Result:" , actual_result)


#add1 is in celeryapp1
###run_task_async(add1 ,(10 ,20), timeout=12)

#function from tasks:

###run_task_async(add1 ,(10 ,20), timeout=12)

###run_task_async(mul ,(2 ,5), timeout=12)

numbers = [[1 ,2 ,3]]
xsum.apply_async(numbers)
###run_task_async(xsum ,(numbers), timeout=12)




