from celery_examples.celery_example_2.celeryapp2 import myapp2
from celery_examples.celery_example_2.tasks import add

params = (10 , 2)
async_result = add.apply_async((params))
res = async_result.get( timeout = 10)
print(res)

#add.send( (params))

