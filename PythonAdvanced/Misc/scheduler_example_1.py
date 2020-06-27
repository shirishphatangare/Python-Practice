#schedule is an in-process scheduler for periodic jobs that uses the builder pattern for
# configuration.It lets you run Python functions (or any other callable) periodically at
# predetermined intervals


#CommandLIne: pip install schedule
import schedule

def job():
    print("A Simple Python Scheduler.")

# run the function job() every 2 seconds
schedule.every(5).seconds.do(job)
#do() specifies the job_func that should be called every time the job runs.

while True:
    schedule.run_pending()