#Python presents us with the crontab module to manage scheduled jobs via Cron
#The functions available in it allow us to access Cron, create jobs, set restrictions, remove jobs, and more.
#CommandLine: pip install python-crontab

#Sample Example:
from crontab import CronTab

cron = CronTab(user='username')
job = cron.new(command='python example1.py')
job.minute.every(1)
cron.write()

#Setting Restrictions
#One of the main advantages of using Python's crontab module is that we can set up time
# restrictions without having to use cron's syntax.
from crontab import CronTab

cron = CronTab(user='username')
job1 = cron.new(command='python scheduler_example_1.py')
job1.hour.every(2)
job2 = cron.new(command='python scheduler_example_1.py')
job2.every(2).hours()
for item in cron:
    print(item)
cron.write()

#we can set the task to be run every time we boot our machine.
job.every_reboot()
#clear all task's restrictions with the following command:
job.clear()
#To enable a job:
job.enable()
#To disable a job:
job.enable(False)
#check whether a task is valid or not with the following command:
job.is_valid()
#Finding a Job: Based on the command Name
cron.find_command("command name")
#Finding a Job: Based on comment
cron.find_comment("comment")
#Finding a Job: Based on time
#cron.find_time(time schedule)

"""
iter1 = cron.find_command('exam')
iter2 = cron.find_comment('comment')
iter3 = cron.find_time("*/1 * * * *")

for item1 in iter1:
    print item1

for item2 in iter2:
    print item2

for item3 in iter3:
    print item3
"""

#Removing Jobs
cron.remove(job)
#Clearing All Jobs
cron.remove_all()