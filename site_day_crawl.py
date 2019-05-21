import requests
from bs4 import BeautifulSoup

url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9C0&stname=%25E5%25A4%25A9%25E6%25AF%258D&datepicker=2018-05-19#"

def fetch(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def parse_data(item):
    array = []
    # array = [it.replace('\xa0','') for it in item if it != '\n']
    for it in item:
        if it != '\n':
            c = it.string.replace('\xa0','')
            try:
                c = float(c)
            except:
                pass
            finally:
                array.append(c)
    return array

soup = fetch(url)

col_name_cn = [name.string for name in soup.select("tr.second_tr")[0] if name.string != '\n']
col_name_en = [name.string for name in soup.select("tr.second_tr")[1] if name.string != '\n']
#len(17)

raw_data = soup.select("tr")[-24:]


