import requests
from bs4 import BeautifulSoup

import csv

def fetch(url):
    res = requests.post(url)  # 可能要用request post form data
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466880&stname=%25E6%259D%25BF%25E6%25A9%258B&datepicker=2019-05-15"

soup = fetch(url)

site = soup.find_all("option")
site = [','.join(item.string.split('_')) for item in site if '撤銷站' not in item]

with open('site_newtaipei', 'w') as f:
    print('station,stname', file=f)
    for item in site:
        print(item, file=f)