#Context Manager
#The second and possibly most popular method of instantiating a ThreadPoolExecutor is using it as a context manager like so:
#with ThreadPoolExecutor(max_workers=3) as executor:
from concurrent.futures import ThreadPoolExecutor

def task(n):
 print("Processing {}".format(n))

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=3) as executor:
   future = executor.submit(task, (2))
   future = executor.submit(task, (3))
   future = executor.submit(task, (4))
 print("All tasks complete")

if __name__ == '__main__':
 main()
