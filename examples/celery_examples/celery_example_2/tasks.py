
from celery_examples.celery_example_2.celeryapp2 import myapp2
import time


add_task_name = "add_task"

@myapp2.task ( name = add_task_name)
def add(x, y):
    time.sleep(2)
    return x + y



if __name__ == '__main__':
    print("after start in main 2")


    print(add(2,2))

    async_result = add.delay(2, 2)

    #This method is actually a star-argument shortcut to another method called apply_async():
    #This is a handy shortcut to the apply_async() method that gives greater control of the task execution (see Calling Tasks):

    print(async_result.ready)