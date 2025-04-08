from login import *
from jobs import Jobs
import time


job_input_by_user = 'Ai developer'


login = Login()
time.sleep(5)
job = Jobs(login.driver)
job.jobs_filter(job_input_by_user)
time.sleep(2)
job.jobsinfo()