from src.services.news_service.applications.cronjob import run_cronjob

if __name__ == '__main__':
    a = input('Enter a number: ')
    if int(a) == 1:
        run_cronjob()
