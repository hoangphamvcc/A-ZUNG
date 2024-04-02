import time
import schedule


def task(arg):
    print('Doing task... ',f'args = {arg}')


schedule.every(3).seconds.do(task,1)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)