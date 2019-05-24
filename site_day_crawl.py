import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, quote_plus
from collections import namedtuple
import csv

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql.expression import insert
from configparser import ConfigParser

# https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp
engine = create_engine("mysql+pymysql://root:andypersonal@127.0.0.1/Weather")

def fetch(url):
    res = requests.post(url)  # 可能要用request post form data
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def parse_special(x):
    '''T 表微量(小於 0.1mm)，x 表故障，V 表風向不定，/表不明，…表無觀測'''
    special = {'T': 0,  # < 0.1mm
               'V': None,  # Undefined
               'x': None,  # Broken Unknown
               'X': None,
               '/': 0,  # Unknown
               '...': None,  # Not observed
               '': 0
               }
    if x in special.keys():
        try:
            return special[x]
        except:
            return 0
    else:
        return x

def parse_data(item):
    array = []
    for it in item:
        if it != '\n':
            c = it.string.replace('\xa0', '')
            try:
                array.append(parse_special(c))
            except:
                array.append(None)
    return array

def pipeline(weather_item):
    meta = MetaData(bind=engine)
    weather_data = Table('WeatherData', meta, autoload=True)
    i = insert(weather_data)
    engine.execute(i.values(weather_item))

# Read dates
with open('date2018') as f:
    dates = f.read().split('\n')
# Read sites
with open('sites') as f:
    sites = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]

for site in sites:
    for date in dates:
        payload = {'station': site['station'],
                   'stname': site['stname'], 'datepicker': date}
        result = urlencode(payload, quote_via=quote_plus)
        url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&{}".format(
            result).replace('%', '%25')
        res = requests.post(url)
        soup = BeautifulSoup(res.text, 'lxml')
        if 'SeaPres' in res.text:
            print("Success!")
            raw_data = soup.select("tr")[-24:]

            col_name_cn = [name.string for name in soup.select(
                "tr.second_tr")[0] if name.string != '\n']
            col_name_en = [name.string for name in soup.select(
                "tr.second_tr")[1] if name.string != '\n']
            for item in raw_data:
                parsed_data = dict(zip(col_name_en, parse_data(item)))

                weather_data = {}
                weather_data.update(payload)
                weather_data.update(parsed_data)  # combine 2 dict

                pipeline(weather_data)
            print(date, site, "Complete")
        else:
            print(date, site, "Crawling Failed!")

# len(17)
