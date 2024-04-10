from applications.cronjob import run_cronjob, request_recent_vn_express_news, send_news_hourly
import src.config

if __name__ == '__main__':
    run_cronjob()
    # request_recent_vn_express_news()
    # send_news_hourly()
