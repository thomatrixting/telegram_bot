import time
from datetime import datetime
import pytz #mange times zones

from send_notification import start_sending

bogota_time_zone = pytz.timezone('America/Bogota')

def execute_in_the_future(days_in_the_furture,f_hour,f_minute):
    """The function takes the current time, and calculates for how many seconds should sleep until a user provided minute in the future."""       
    t = datetime.today()
    future = datetime(t.year,t.month,t.day + days_in_the_furture,f_hour,f_minute)
    if future.minute <= t.minute or future.hour < t.hour:
        print("ERROR! Enter a valid time in the future.")
    else:
        print (f"Current time: {t.day} : {t.hour} : {t.minute}")
        print (f"Sleep until :  {future.day} : {future.hour} : {future.minute}")
        seconds_till_future = (future-t).seconds

        time.sleep( seconds_till_future )
        start_sending()

if __name__ == "__main__":
    execute_in_the_future(0,15,50)
    while True:
       execute_in_the_future(1,7,30)
    
        