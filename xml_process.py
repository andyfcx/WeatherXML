from bs4 import BeautifulSoup
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql.expression import insert
import pandas as pd

with open('mn_Report_2018.xml') as f:
    xml = f.read()
soup = BeautifulSoup(xml, 'lxml')

time_item = soup.find_all('time') 

# parse every month and save to file
for item in time_item:
    filename = item.find('datatime').string

    with open(f'xml_weather/{filename}.xml','w') as f:
        print(item, file=f) 
        print(f"{filename} FIN" )
