#
#Example file for formatting time and date output
#
from datetime import datetime
def main():
   #Times and dates can be formatted using a set of predefined string

   #Control codes
      now= datetime.now() #get the current date and time
      #%c - local date and time, %x-local's date, %X- local's time
      print(now.strftime("%c"))
      print(now.strftime("%x"))
      print(now.strftime("%X"))

##### Time Formatting ####
      #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
      print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
      print(now.strftime("%H:%M")) # 24-Hour:Minute

if __name__== "__main__":
    main()