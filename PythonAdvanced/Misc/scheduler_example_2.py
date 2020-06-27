#Other Variations of the schedule

import schedule
import time

def job():
    print("I'm working...")

def job3(name):
    print("Hello:"+name+" from job3")

"""

schedule.every(5).seconds.do(job)
# some other variations
schedule.every().hour.do(job)
schedule.every().day.at("12:25").do(job)
#By default schedule uses 24 hr format.
schedule.every(5).to(10).minutes.do(job)
#This one executes job() every 5 to 10 minutes ;)
schedule.every().thursday.at("19:15").do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

"""


schedule.every(2).seconds.do(job3,"SSS")

while True:
    schedule.run_pending()
    time.sleep(1)

# run the function job() every 2 seconds
schedule.every(2).seconds.do(job)
#do() specifies the job_func that should be called every time the job runs.

while True:
    schedule.run_pending()