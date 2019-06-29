from celery import Celery
from urllib.parse import urlencode, quote_plus
from site_day_crawl import crawl
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')
rabbitmq_host = config.get('rabbitmq', 'host')
rabbitmq_user = config.get('rabbitmq', 'user')
rabbitmq_pwd = config.get('rabbitmq', 'password')

app = Celery('tasks',
             broker='pyamqp://{}:{}@{}//'.format(rabbitmq_user, rabbitmq_pwd, rabbitmq_host)
             )


@app.task(queue="Weather")
def job(site, date):
    crawl(site, date)


@app.task(queue="examine")
def hello(site, date):
    # celery -A tasks worker -Q examine
    payload = {'station': site['station'],
               'stname': site['stname'], 'datepicker': date}
    result = urlencode(payload, quote_via=quote_plus)
    url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&{}".format(
        result).replace('%', '%25')
    print(url)
    # print(type(site), type(date))
