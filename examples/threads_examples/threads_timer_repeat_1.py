import threading

def printit():
  interval = 2.0
  #send printit itself as the function
  threading.Timer(interval, printit).start()
  print ("Hello, World!")

printit()