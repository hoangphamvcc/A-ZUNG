from crontab import CronTab
my_cron = CronTab(user='user')
job = my_cron.new(command='python3 /home/user/test/producers.py')
job.minute.every(1)

my_cron.write()

