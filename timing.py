
import schedule
import time
import random
import datetime
timeleft = 60
time_change = datetime.timedelta(minutes=1)
from datetime import datetime, date


#datetime.combine(date.today(), exit) - datetime.combine(date.today(), enter)
#print((dt_ended - dt_started).total_seconds())


def job():
    global time_change
    now = datetime.now()
    current_time = datetime.strptime(now.strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
    target_time = current_time + time_change
    print(target_time)

    print("the target time is: ", target_time)
    print((target_time - now).total_seconds())

    print ("I'm working...")
    return

def adjustwait():
    now = datetime.now()
    current_time = datetime.strptime(now.strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
    target_time = current_time + time_change
    timetoexecute = (target_time - now).total_seconds()
    if timetoexecute < 5:
        time.sleep(5)
        return
    else:
        return


schedule.every().minutes.do(job)
schedule.every().sunday.at("16:59").do(job)
schedule.every().saturday.at("19:55:00").do(job)


while True:
    now = datetime.now()
    print(now)
    schedule.run_pending()
    now = datetime.now()
    print(now)
    time.sleep(50)
    #adjustwait()

'''
from datetime import datetime, timedelta

# datetime object containing current date and time
now = datetime.now()
time_change = datetime.timedelta(seconds=10)
date_and_time = now + time_change

#import datetime
#date_and_time = datetime.datetime(2021, 9, 11, 13, 33, 0)
#ime_change = datetime.timedelta(seconds=10)
print(date_and_time)
print(time_change)
print(date_and_time+time_change)
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

from datetime import date
from apscheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def my_job(text):
    print (text)

# The job will be executed on November 6th, 2009
exec_date = date(2009, 11, 6)

# Store the job in a variable in case we want to cancel it
#job = sched.add_date_job(my_job, exec_date, ['text'])

job = sched.add_date_job(my_job, datetime(2021, 9, 11, 13, 42, 0), ['executed'])
'''